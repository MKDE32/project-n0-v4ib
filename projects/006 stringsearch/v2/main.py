import os
import sys
import re


def clean_path(p):
    return p.strip().strip('"').strip("'")


def build_search_pattern(term, split_search=False):
    if split_search:
        # htb -> h[\W_]*t[\W_]*b
        return re.compile(
            r"[\W_]*".join(map(re.escape, term)),
            re.IGNORECASE
        )
    else:
        return re.compile(re.escape(term), re.IGNORECASE)


def search_in_files(root_dir, search_term, split_search=False):
    matches = []

    pattern = build_search_pattern(search_term, split_search)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        if pattern.search(line):
                            matches.append(
                                (filepath, line_num, line.strip())
                            )

            except Exception:
                pass

    return matches


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("python3 script.py '<directory>' <search_term> [--split]")
        sys.exit(1)

    directory = clean_path(sys.argv[1])
    term = sys.argv[2]

    split_mode = "--split" in sys.argv

    if not os.path.exists(directory):
        print(f"[!] Path does not exist: {directory}")
        sys.exit(1)

    results = search_in_files(
        directory,
        term,
        split_mode
    )

    if results:
        print(f"\n[+] Found {len(results)} matches:\n")

        for file, line, content in results:
            print(f"{file} (line {line}): {content}")

    else:
        print("\n[-] No matches found.")
