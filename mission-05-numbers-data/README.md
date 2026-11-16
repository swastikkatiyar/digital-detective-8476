### Task 5.1: Convert Numbers by Hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | $13 \div 2 = 6$ remainder $1$<br>$6 \div 2 = 3$ remainder $0$<br>$3 \div 2 = 1$ remainder $1$<br>$1 \div 2 = 0$ remainder $1$<br>**Answer:** `1101₂` |
| **Convert decimal 25 to binary.** | $25 \div 2 = 12$ remainder $1$<br>$12 \div 2 = 6$ remainder $0$<br>$6 \div 2 = 3$ remainder $0$<br>$3 \div 2 = 1$ remainder $1$<br>$1 \div 2 = 0$ remainder $1$<br>**Answer:** `11001₂` |
| **Convert binary 1010 to decimal.** | $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>$= 8 + 0 + 2 + 0$<br>**Answer:** `10₁₀` |
| **Convert binary 1101 to decimal.** | $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>$= 8 + 4 + 0 + 1$<br>**Answer:** `13₁₀` |
| **Convert hexadecimal A to decimal.** | In hexadecimal, $A = 10$[cite: 10].<br>$(10 \times 16^0) = 10 \times 1$<br>**Answer:** `10₁₀` |
| **Convert hexadecimal 1F to decimal.** | $(1 \times 16^1) + (15 \times 16^0)$ where $F = 15$[cite: 10].<br>$= 16 + 15$<br>**Answer:** `31₁₀` |
| **Convert binary 1111 to hexadecimal.** | Group bits from right: `1111₂` = $8 + 4 + 2 + 1 = 15_{10}$.<br>In hexadecimal, decimal $15 = F$[cite: 10].<br>**Answer:** `F₁₆` |


### Task 5.2: Verify Using Python

| Expression tested | Python result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101₂`) |
| `bin(25)` | `'0b11001'` | Yes (`11001₂`) |
| `int('1010', 2)` | `10` | Yes (`10₁₀`) |
| `int('1101', 2)` | `13` | Yes (`13₁₀`) |
| `int('A', 16)` | `10` | Yes (`10₁₀`) |
| `int('1F', 16)` | `31` | Yes (`31₁₀`) |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`F₁₆`) |


### Task 5.3
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **10** | `'0b1010'`[cite: 10] | `'0xa'`[cite: 10] |
| **25** | `'0b11001'`[cite: 10] | `'0x19'`[cite: 10] |
| **255** | `'0b11111111'`[cite: 10] | `'0xff'`[cite: 10] |