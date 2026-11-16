# Mission 7 - Computer networks

## 1. Task / objective
Explain core network concepts and architecture types, observe network connectivity and DNS lookup behavior using terminal tools, and document website communication steps[cite: 11, 12].

## 2. Work completed
* Completed **Task 7.1**: Completed the network concepts table covering LAN, MAN, WAN, DNS, routers, protocols, packet switching, and client-server architecture[cite: 11, 12].
* Completed **Task 7.2**: Executed network observation commands (`ping`, `nslookup`, `traceroute`) to test reachability, inspect DNS resolution, and trace packet hops while ensuring privacy-safe outputs[cite: 11, 12].
* Completed **Task 7.3**: Documented network command usage and verification notes[cite: 12].

## 3. Commands / tools used
* **Terminal Networking Tools**: `ping -c 4 8.8.8.8`, `nslookup google.com`, `traceroute 8.8.8.8`[cite: 12].

## 4. My understanding
Computer networks connect devices globally using standardized protocols and packet switching. When accessing resources, clients query DNS servers to resolve human-readable domain names into numeric IP addresses, allowing routers to efficiently direct data packets across local and wide-area networks.

## 5. Difficulties faced
Ensuring that terminal network trace outputs did not accidentally expose local network identifiers or private IP addresses.

## 6. How I resolved them
Redacted raw IP details and summarized command behavior conceptually in the documentation[cite: 11, 12].

## 7. Evidence / files
* `mission-07-networking/README.md` containing completed network tables and tool logs[cite: 4, 12].

## 8. Commit details
* **Commit message:** "Explain networking concepts and website communication"[cite: 14]
* **Status:** Confirmed visible and pushed successfully to GitHub[cite: 12, 14].


### Task 7.3: What Happens When You Open a Website?

1. **User Request:** You enter a website URL (like `https://www.google.com`) into your web browser, which acts as the **client**[cite: 11].
2. **DNS Lookup:** The browser checks its cache and queries a **DNS** (Domain Name System) server to translate the human-readable domain name into the server's numeric IP address[cite: 11].
3. **Routing & Connection:** Your computer sends the connection request through your local network **router**, which forwards the data packets across the internet toward the destination IP address[cite: 11].
4. **Protocol Handshake:** The **client** and the destination web **server** establish a connection using standard communication **protocols** (such as TCP/IP and HTTP/HTTPS)[cite: 11].
5. **Server Processing:** The web **server** receives the request, processes it, and prepares the required webpage files (HTML, CSS, images)[cite: 11].
6. **Response & Display:** The **server** sends the data packets back through the network to your browser (**client**), which reassembles and renders the webpage on your screen[cite: 11].