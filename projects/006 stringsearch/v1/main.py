import os
import sys

def clean_path(p):
    return p.strip().strip('"').strip("'")

def search_in_files(root_dir, search_term):
    matches = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        if search_term.lower() in line.lower():
                            matches.append((filepath, line_num, line.strip()))
            except Exception:
                # ignore binary / unreadable files
                pass

    return matches


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py '<directory>' <search_term>")
        sys.exit(1)

    directory = clean_path(sys.argv[1])
    term = sys.argv[2]

    if not os.path.exists(directory):
        print(f"[!] Path does not exist: {directory}")
        sys.exit(1)

    results = search_in_files(directory, term)

    if results:
        print(f"\n[+] Found {len(results)} matches:\n")
        for file, line, content in results:
            print(f"{file} (line {line}): {content}")
    else:
        print("\n[-] No matches found.")
