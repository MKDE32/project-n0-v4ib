```
using System;
using System.Net;
using System.Net.Sockets;

class Program
{
    static void Main()
    {
        UdpClient server = new UdpClient(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 53));
        IPEndPoint upstream = new IPEndPoint(IPAddress.Parse("8.8.8.8"), 53);

        while (true)
        {
            IPEndPoint clientEP = new IPEndPoint(IPAddress.Any, 0);
            byte[] data = server.Receive(ref clientEP);

            UdpClient upstreamClient = new UdpClient();
            upstreamClient.Send(data, data.Length, upstream);

            byte[] response = upstreamClient.Receive(ref upstream);

            server.Send(response, response.Length, clientEP);

            upstreamClient.Close();
        }
    }
}
```
