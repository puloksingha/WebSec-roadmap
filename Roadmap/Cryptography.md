Cryptography Roadmap for Cybersecurity

Phase 1: Cryptography Fundamentals

1. Introduction to Cryptography

- [ ] What is cryptography?
- [ ] History of cryptography
- [ ] Why cryptography is important
- [ ] Cryptography vs encryption
- [ ] Cryptography vs cryptanalysis
- [ ] Cryptography vs steganography
- [ ] Plaintext and ciphertext
- [ ] Encryption and decryption
- [ ] Cryptographic keys
- [ ] Algorithms and protocols
- [ ] Cryptographic attacks
- [ ] Key management

2. Security Principles

- [ ] Confidentiality
- [ ] Integrity
- [ ] Authentication
- [ ] Non-repudiation
- [ ] Availability
- [ ] Data protection
- [ ] Secure communication
- [ ] Defense in depth

3. Mathematical Foundations

- [ ] Binary numbers
- [ ] Decimal, hexadecimal, and octal
- [ ] Binary-to-hexadecimal conversion
- [ ] Modular arithmetic
- [ ] Prime numbers
- [ ] Greatest common divisor (GCD)
- [ ] Euclidean algorithm
- [ ] Extended Euclidean algorithm
- [ ] Multiplicative inverse
- [ ] Exponents and logarithms
- [ ] Probability basics
- [ ] Random numbers
- [ ] XOR operations
- [ ] Bitwise operations

Phase 2: Classical Cryptography

4. Classical Encryption Techniques

- [ ] Caesar cipher
- [ ] Substitution cipher
- [ ] Monoalphabetic cipher
- [ ] Polyalphabetic cipher
- [ ] Vigenère cipher
- [ ] Playfair cipher
- [ ] Hill cipher
- [ ] Transposition cipher
- [ ] Rail Fence cipher
- [ ] One-Time Pad (OTP)

5. Classical Cryptanalysis

- [ ] Brute-force attacks
- [ ] Frequency analysis
- [ ] Known-plaintext attacks
- [ ] Chosen-plaintext attacks
- [ ] Chosen-ciphertext attacks
- [ ] Ciphertext-only attacks
- [ ] Limitations of classical encryption

Phase 3: Modern Cryptography

6. Symmetric-Key Cryptography

Understand how the same secret key is used for encryption and decryption.

- [ ] Symmetric encryption fundamentals
- [ ] Block ciphers
- [ ] Stream ciphers
- [ ] Data Encryption Standard (DES)
- [ ] Triple DES (3DES)
- [ ] Advanced Encryption Standard (AES)
- [ ] AES-128, AES-192, AES-256
- [ ] AES encryption modes
- [ ] ECB mode
- [ ] CBC mode
- [ ] CTR mode
- [ ] GCM mode
- [ ] Initialization Vectors (IV)
- [ ] Nonces
- [ ] Padding
- [ ] Key sizes
- [ ] Authenticated encryption
- [ ] Authenticated Encryption with Associated Data (AEAD)

Important: Understand why ECB is insecure for general data encryption and why AES-GCM is a common modern choice.

7. Asymmetric-Key Cryptography

Understand public-key and private-key cryptography.

- [ ] Public and private keys
- [ ] RSA
- [ ] RSA key generation
- [ ] RSA encryption and decryption
- [ ] RSA signatures
- [ ] Diffie-Hellman key exchange
- [ ] Elliptic Curve Cryptography (ECC)
- [ ] Elliptic Curve Diffie-Hellman (ECDH)
- [ ] Elliptic Curve Digital Signature Algorithm (ECDSA)
- [ ] Ed25519
- [ ] Digital signatures
- [ ] Key exchange
- [ ] Hybrid encryption

8. Hashing Algorithms

Understand one-way cryptographic functions.

- [ ] What is hashing?
- [ ] Hashing vs encryption
- [ ] Properties of cryptographic hashes
- [ ] Collision resistance
- [ ] Preimage resistance
- [ ] Second-preimage resistance
- [ ] MD5
- [ ] SHA-1
- [ ] SHA-2
- [ ] SHA-256
- [ ] SHA-512
- [ ] SHA-3
- [ ] BLAKE2
- [ ] BLAKE3
- [ ] Hash collisions
- [ ] Avalanche effect
- [ ] Hash length and digest

9. Password Security

- [ ] Password storage
- [ ] Password hashing
- [ ] Password salting
- [ ] Peppering
- [ ] Brute-force attacks
- [ ] Dictionary attacks
- [ ] Rainbow tables
- [ ] Password cracking concepts
- [ ] PBKDF2
- [ ] bcrypt
- [ ] scrypt
- [ ] Argon2
- [ ] Password strength
- [ ] Secure password reset
- [ ] Multi-factor authentication

Important: Passwords should be stored using dedicated password-hashing algorithms such as Argon2id, bcrypt, or scrypt, not plain SHA-256 or MD5.

Phase 4: Message Authentication and Integrity

10. Message Authentication

- [ ] Message Authentication Codes (MAC)
- [ ] HMAC
- [ ] HMAC-SHA256
- [ ] CMAC
- [ ] Message integrity
- [ ] Authentication tags
- [ ] Keyed vs unkeyed hashing
- [ ] Timing-safe comparison

11. Digital Signatures

- [ ] Digital signature fundamentals
- [ ] Signing and verification
- [ ] RSA signatures
- [ ] RSA-PSS
- [ ] ECDSA signatures
- [ ] EdDSA
- [ ] Certificate-based signatures
- [ ] Signature verification
- [ ] Signature forgery concepts

Phase 5: PKI and Digital Certificates

12. Public Key Infrastructure (PKI)

- [ ] What is PKI?
- [ ] Certificate Authority (CA)
- [ ] Root CA
- [ ] Intermediate CA
- [ ] Digital certificates
- [ ] X.509 certificate format
- [ ] Certificate signing requests (CSR)
- [ ] Certificate chains
- [ ] Certificate validation
- [ ] Certificate revocation
- [ ] CRL
- [ ] OCSP
- [ ] Self-signed certificates
- [ ] Certificate pinning
- [ ] Public and private key storage

13. SSL/TLS Security

- [ ] SSL vs TLS
- [ ] TLS 1.2
- [ ] TLS 1.3
- [ ] TLS handshake
- [ ] Cipher suites
- [ ] Key exchange
- [ ] Server authentication
- [ ] Client authentication
- [ ] Forward secrecy
- [ ] HTTPS
- [ ] Certificate validation
- [ ] TLS vulnerabilities
- [ ] HSTS
- [ ] Secure cookie attributes
- [ ] Certificate misconfiguration

Phase 6: Cryptographic Attacks

14. Common Cryptographic Attacks

- [ ] Brute-force attacks
- [ ] Dictionary attacks
- [ ] Birthday attacks
- [ ] Collision attacks
- [ ] Padding oracle attacks
- [ ] Replay attacks
- [ ] Man-in-the-middle attacks
- [ ] Downgrade attacks
- [ ] Weak random number generation
- [ ] Weak key generation
- [ ] Nonce reuse
- [ ] IV reuse
- [ ] Side-channel attacks
- [ ] Timing attacks
- [ ] Cache attacks
- [ ] Fault injection
- [ ] Key leakage
- [ ] Insecure cryptographic implementations

15. Advanced Cryptographic Concepts

- [ ] Perfect forward secrecy
- [ ] Zero-Knowledge Proofs
- [ ] Homomorphic encryption
- [ ] Secure Multi-Party Computation
- [ ] Threshold cryptography
- [ ] Post-Quantum Cryptography
- [ ] Quantum computing and cryptography
- [ ] Lattice-based cryptography
- [ ] Key derivation functions
- [ ] HKDF
- [ ] Cryptographic random number generators

Phase 7: Cryptography in Web Application Security

16. Web Application Cryptography

- [ ] HTTPS implementation
- [ ] TLS certificate configuration
- [ ] Password storage in databases
- [ ] Session token security
- [ ] JWT structure
- [ ] JWT signing algorithms
- [ ] HMAC-based JWT
- [ ] RSA-based JWT
- [ ] ECDSA-based JWT
- [ ] JWT signature verification
- [ ] JWT algorithm confusion
- [ ] Insecure JWT validation
- [ ] Cookie security
- [ ] CSRF tokens
- [ ] API authentication
- [ ] API key security
- [ ] Secure password reset tokens
- [ ] Secure random token generation
- [ ] Data encryption at rest
- [ ] Data encryption in transit
- [ ] Secrets management
- [ ] Cryptographic implementation mistakes

17. OWASP-Related Cryptographic Risks

- [ ] Cryptographic failures
- [ ] Weak encryption algorithms
- [ ] Hardcoded encryption keys
- [ ] Hardcoded API secrets
- [ ] Weak password hashing
- [ ] Insecure random number generation
- [ ] Missing HTTPS
- [ ] Improper certificate validation
- [ ] Insecure TLS configuration
- [ ] Improper encryption key management
- [ ] Sensitive data exposure
- [ ] Improper cryptographic implementation

Phase 8: Practical Tools and Commands

18. Linux Cryptography Tools

- [ ] OpenSSL
- [ ] GnuPG (GPG)
- [ ] Hash utilities
- [ ] Base64 encoding and decoding
- [ ] xxd
- [ ] hexdump
- [ ] strings
- [ ] John the Ripper
- [ ] Hashcat
- [ ] CyberChef
- [ ] Python hashlib
- [ ] Python cryptography library

19. Practical Projects

- [ ] Build a Caesar cipher program
- [ ] Build a Vigenère cipher program
- [ ] Create a file hashing utility
- [ ] Build a SHA-256 integrity checker
- [ ] Create an AES encryption/decryption tool
- [ ] Generate RSA keys
- [ ] Create and verify digital signatures
- [ ] Build a password-hashing demonstration
- [ ] Inspect an HTTPS certificate
- [ ] Analyze JWT tokens
- [ ] Build a secure token generator
- [ ] Create a secure file-encryption utility

Phase 9: Learning Resources

- [ ] Cryptohack
- [ ] Crypto 101
- [ ] Cryptopals Challenges
- [ ] OpenSSL Documentation
- [ ] Python Cryptography Documentation
- [ ] OWASP Cryptographic Storage Cheat Sheet
- [ ] PortSwigger Web Security Academy
- [ ] NIST Cryptographic Standards

Suggested Study Schedule

Week| Topics
1| Fundamentals and mathematics
2| Classical cryptography
3| Symmetric encryption
4| Asymmetric encryption
5| Hashing, MACs, and password security
6| Digital signatures and PKI
7| TLS and cryptographic attacks
8| Web application cryptography and projects

Final Readiness Checklist

- [ ] Explain encryption, hashing, and encoding.
- [ ] Understand AES and RSA.
- [ ] Explain public/private keys.
- [ ] Understand SHA-256 and HMAC.
- [ ] Explain password salting and password hashing.
- [ ] Understand JWT signing and validation.
- [ ] Explain HTTPS and TLS handshakes.
- [ ] Inspect X.509 certificates.
- [ ] Identify weak cryptographic implementations.
- [ ] Complete at least three practical cryptography projects.

Final goal: Understand how cryptography works, how developers implement it, and how implementation mistakes create security vulnerabilities.
