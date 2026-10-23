# Python Roadmap for Cybersecurity, Web Security & Application Security

## Phase 1: Python Fundamentals Revision

### 1. Python Environment and Setup
- [ ] Installing and checking Python
- [ ] Python interpreter and interactive shell
- [ ] Running Python scripts from the terminal
- [ ] Using an IDE or code editor
- [ ] Python indentation and syntax
- [ ] Comments and docstrings
- [ ] Understanding tracebacks and error messages
- [ ] Using `help()` and `dir()`
- [ ] Python virtual environments (`venv`)
- [ ] Installing packages using `pip`
- [ ] `requirements.txt`
- [ ] Understanding Python versions and package compatibility

### 2. Variables and Data Types
- [ ] Variables and naming conventions
- [ ] Dynamic typing
- [ ] Integers and floating-point numbers
- [ ] Strings
- [ ] Booleans
- [ ] Type conversion and casting
- [ ] `None` and `NoneType`
- [ ] Checking types with `type()` and `isinstance()`
- [ ] Mutable vs. immutable objects
- [ ] Identity vs. equality (`is` vs. `==`)

### 3. Operators
- [ ] Arithmetic operators
- [ ] Comparison operators
- [ ] Logical operators
- [ ] Assignment operators
- [ ] Membership operators (`in`, `not in`)
- [ ] Identity operators (`is`, `is not`)
- [ ] Operator precedence
- [ ] Bitwise operators (basic understanding)

### 4. Conditional Statements
- [ ] `if`, `elif`, and `else`
- [ ] Nested conditions
- [ ] Truthy and falsy values
- [ ] Conditional expressions
- [ ] Combining logical conditions
- [ ] Input validation with conditions

### 5. Loops
- [ ] `for` loops
- [ ] `while` loops
- [ ] `range()`
- [ ] `break` and `continue`
- [ ] The `pass` statement
- [ ] Nested loops
- [ ] Looping through collections
- [ ] Loop control and termination conditions
- [ ] Avoiding infinite loops

### 6. Strings
- [ ] String indexing and slicing
- [ ] String immutability
- [ ] String methods
- [ ] Searching and replacing text
- [ ] Splitting and joining strings
- [ ] String formatting and f-strings
- [ ] Escape sequences
- [ ] Unicode and character encoding basics
- [ ] Working with multiline strings
- [ ] Parsing structured text

### 7. Lists, Tuples, Sets, and Dictionaries
- [ ] Creating and accessing lists
- [ ] List indexing and slicing
- [ ] List methods
- [ ] List comprehensions
- [ ] Nested lists
- [ ] Creating and unpacking tuples
- [ ] Sets and set operations
- [ ] Creating and accessing dictionaries
- [ ] Dictionary methods
- [ ] Iterating over keys, values, and items
- [ ] Dictionary comprehensions
- [ ] Nested dictionaries
- [ ] Unpacking collections
- [ ] Shallow copies vs. references
- [ ] Shallow copy vs. deep copy

### 8. Functions
- [ ] Defining and calling functions
- [ ] Parameters and arguments
- [ ] Positional and keyword arguments
- [ ] Default parameters
- [ ] `*args` and `**kwargs`
- [ ] Return values
- [ ] Scope and namespaces
- [ ] Local and global variables
- [ ] Lambda functions
- [ ] Recursion
- [ ] First-class functions
- [ ] Basic higher-order functions
- [ ] Type hints
- [ ] Docstrings
- [ ] Writing reusable functions

### 9. Exception Handling
- [ ] Syntax errors vs. runtime errors
- [ ] Common built-in exceptions
- [ ] `try` and `except`
- [ ] Handling multiple exceptions
- [ ] `else` and `finally`
- [ ] Raising exceptions with `raise`
- [ ] Creating custom exceptions
- [ ] Debugging tracebacks
- [ ] Avoiding overly broad exception handling
- [ ] Safe error messages and logging

---

## Phase 2: Intermediate Python

### 10. File Handling
- [ ] Opening and closing files
- [ ] Context managers with `with`
- [ ] Reading and writing text files
- [ ] Appending to files
- [ ] File modes
- [ ] File paths using `pathlib`
- [ ] Working with directories
- [ ] Handling missing files and permissions
- [ ] Reading large files efficiently
- [ ] File encoding
- [ ] Binary file handling
- [ ] Temporary files and directories

### 11. Modules and Packages
- [ ] Importing modules
- [ ] Standard library overview
- [ ] Creating custom modules
- [ ] Creating packages
- [ ] `__name__ == "__main__"`
- [ ] Absolute and relative imports
- [ ] Module search paths
- [ ] Package organization
- [ ] Dependency management
- [ ] Avoiding circular imports

### 12. Object-Oriented Programming (OOP)
- [ ] Classes and objects
- [ ] Attributes and methods
- [ ] Instance and class attributes
- [ ] Constructors with `__init__`
- [ ] Instance, class, and static methods
- [ ] Encapsulation
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Method overriding
- [ ] `super()`
- [ ] Properties and `@property`
- [ ] Special methods and dunder methods
- [ ] Composition vs. inheritance
- [ ] Dataclasses
- [ ] Abstract base classes (basic understanding)

### 13. Iterators and Generators
- [ ] Iterables and iterators
- [ ] `iter()` and `next()`
- [ ] Generator functions
- [ ] `yield`
- [ ] Generator expressions
- [ ] Lazy evaluation
- [ ] Memory-efficient processing
- [ ] Writing generators for large log files

### 14. Comprehensions and Functional Tools
- [ ] List comprehensions
- [ ] Dictionary comprehensions
- [ ] Set comprehensions
- [ ] Nested comprehensions
- [ ] `map()`
- [ ] `filter()`
- [ ] `zip()`
- [ ] `enumerate()`
- [ ] `sorted()` and custom sort keys
- [ ] `any()` and `all()`
- [ ] Choosing readability over unnecessary complexity

### 15. Regular Expressions
- [ ] Regex syntax and patterns
- [ ] Character classes
- [ ] Quantifiers
- [ ] Anchors and boundaries
- [ ] Groups and capturing groups
- [ ] Alternation
- [ ] Greedy vs. non-greedy matching
- [ ] `re.search()`
- [ ] `re.match()`
- [ ] `re.fullmatch()`
- [ ] `re.findall()`
- [ ] `re.finditer()`
- [ ] `re.sub()`
- [ ] Compiled patterns
- [ ] Raw strings
- [ ] Extracting indicators and patterns from logs
- [ ] Understanding regex performance risks

### 16. Data Formats and Serialization
- [ ] JSON with the `json` module
- [ ] CSV with the `csv` module
- [ ] Reading and writing structured data
- [ ] Converting between dictionaries and JSON
- [ ] Handling malformed input
- [ ] Basic XML parsing
- [ ] URL encoding and decoding
- [ ] Base64 encoding and decoding
- [ ] Bytes vs. strings
- [ ] UTF-8 and other encoding considerations
- [ ] Safe deserialization principles
- [ ] Why untrusted `pickle` data must not be loaded

### 17. Dates, Times, and Data Processing
- [ ] `datetime`
- [ ] Parsing timestamps
- [ ] Time zones and UTC
- [ ] Timestamp comparisons
- [ ] Sorting events chronologically
- [ ] Counting and grouping events
- [ ] Basic statistics
- [ ] Processing security-event timelines

---

## Phase 3: Python for Automation and Command-Line Tools

### 18. Command-Line Programming
- [ ] `sys.argv`
- [ ] `argparse`
- [ ] Positional and optional arguments
- [ ] Flags and switches
- [ ] Input validation
- [ ] Help messages
- [ ] Exit codes
- [ ] Standard output and standard error
- [ ] Reading from standard input
- [ ] Building reusable command-line tools

### 19. Operating-System Interaction
- [ ] `os`
- [ ] `pathlib`
- [ ] `shutil`
- [ ] `subprocess`
- [ ] Environment variables
- [ ] File permissions and metadata
- [ ] Working with processes
- [ ] Executing external commands safely
- [ ] Capturing command output
- [ ] Handling subprocess timeouts and failures
- [ ] Avoiding shell injection
- [ ] Working with temporary files
- [ ] Cross-platform path handling

### 20. Bash and Python Integration
- [ ] Running Python scripts from Bash
- [ ] Passing command-line arguments
- [ ] Using exit codes
- [ ] Pipes and redirection
- [ ] Environment variables
- [ ] Processing logs with `grep`, `awk`, and `sed`
- [ ] Calling Python tools from shell scripts
- [ ] Automating repeatable lab tasks
- [ ] Handling errors in combined workflows

### 21. Logging and Debugging
- [ ] The `logging` module
- [ ] Log levels
- [ ] Log formatting
- [ ] Logging to files
- [ ] Exception tracebacks
- [ ] `pdb` basics
- [ ] IDE debugging
- [ ] Assertions
- [ ] Diagnosing unexpected results
- [ ] Avoiding secrets in logs
- [ ] Structured logging fundamentals

---

## Phase 4: Networking and HTTP Programming

### 22. Networking Fundamentals in Python
- [ ] IP addresses and ports
- [ ] TCP vs. UDP
- [ ] The `socket` module
- [ ] Client-server communication
- [ ] DNS resolution basics
- [ ] Connection timeouts
- [ ] Socket errors
- [ ] Reading and sending data
- [ ] Basic network protocol concepts
- [ ] Safe networking in authorized environments

### 23. HTTP Programming
- [ ] HTTP request and response structure
- [ ] Methods and status codes
- [ ] Headers and content types
- [ ] Query parameters
- [ ] Request bodies
- [ ] Cookies and sessions
- [ ] Redirects
- [ ] Timeouts
- [ ] Response handling
- [ ] Error handling
- [ ] `requests` library
- [ ] Persistent sessions with `requests.Session`
- [ ] TLS certificate verification
- [ ] Proxy configuration
- [ ] Rate limiting and retry strategies
- [ ] Handling API errors

### 24. API Interaction
- [ ] REST API fundamentals
- [ ] JSON requests and responses
- [ ] API authentication concepts
- [ ] API keys and environment variables
- [ ] Pagination
- [ ] Filtering and query parameters
- [ ] Token handling
- [ ] API client design
- [ ] Input validation
- [ ] Response validation
- [ ] Error and timeout handling
- [ ] Testing your own APIs
- [ ] Secure handling of API credentials

---

## Phase 5: Python for Web Security

### 25. HTML and Web Data Processing
- [ ] HTML structure and DOM basics
- [ ] Parsing HTML with Beautiful Soup
- [ ] Extracting links and form fields
- [ ] Understanding form actions and methods
- [ ] URL parsing with `urllib.parse`
- [ ] Query-string parsing
- [ ] HTML entities and encoding
- [ ] Handling malformed HTML
- [ ] Respecting access restrictions and testing scope

### 26. Web Security Concepts to Understand in Code
- [ ] Authentication and authorization
- [ ] Session handling
- [ ] Cookies and cookie attributes
- [ ] CSRF protections
- [ ] CORS configuration
- [ ] Input validation and output encoding
- [ ] SQL injection causes and prevention
- [ ] XSS causes and prevention
- [ ] SSRF risks and mitigations
- [ ] Path traversal
- [ ] File upload security
- [ ] Security headers
- [ ] Rate limiting
- [ ] API authorization
- [ ] Secure error handling

### 27. Python Security Libraries and Utilities
- [ ] `hashlib` for hashing
- [ ] `secrets` for secure random values
- [ ] `hmac` for message authentication
- [ ] `ssl` for TLS-related functionality
- [ ] `ipaddress` for IP address handling
- [ ] `urllib.parse` for URL parsing
- [ ] `requests` for HTTP communication
- [ ] `json` for structured data
- [ ] `re` for text and log analysis
- [ ] `socket` for networking fundamentals
- [ ] `pytest` for testing
- [ ] `cryptography` for appropriate cryptographic operations

**Important:** Learn established cryptographic libraries and secure patterns. Do not invent your own encryption algorithms.

---

## Phase 6: Python for Application Security

### 28. Secure Python Coding
- [ ] Input validation
- [ ] Output encoding where applicable
- [ ] Parameterized database queries
- [ ] Safe file handling
- [ ] Path traversal prevention
- [ ] Avoiding command injection
- [ ] Secure temporary-file handling
- [ ] Secret management
- [ ] Safe exception handling
- [ ] Avoiding sensitive information disclosure
- [ ] Dependency security
- [ ] Secure random-number generation
- [ ] Password hashing principles
- [ ] Secure session and token handling
- [ ] Avoiding unsafe deserialization
- [ ] Secure defaults

### 29. Database Programming
- [ ] SQL fundamentals
- [ ] SQLite with Python
- [ ] Database connections
- [ ] CRUD operations
- [ ] Parameterized queries
- [ ] Transactions
- [ ] Error handling
- [ ] Connection management
- [ ] ORM fundamentals
- [ ] Database access control
- [ ] Database credentials and secrets
- [ ] Understanding SQL injection prevention

### 30. Web Framework Fundamentals
- [ ] How web frameworks work
- [ ] Routing and request handling
- [ ] Middleware
- [ ] Request validation
- [ ] Authentication and authorization
- [ ] Session management
- [ ] Database integration
- [ ] Error handling
- [ ] Logging
- [ ] Testing endpoints
- [ ] Security configuration
- [ ] API documentation

**Frameworks to consider:**
- Flask: lightweight and useful for understanding web fundamentals.
- Django: useful for learning an integrated framework with built-in security features.
- FastAPI: useful for building modern APIs with validation and type hints.

You do not need to master all three. Choose one based on your existing development knowledge and project goals.

---

## Phase 7: Testing, Quality, and Code Analysis

### 31. Automated Testing
- [ ] `unittest`
- [ ] `pytest`
- [ ] Test cases and assertions
- [ ] Fixtures
- [ ] Mocking
- [ ] Testing functions and modules
- [ ] Testing API endpoints
- [ ] Testing invalid inputs
- [ ] Testing authorization rules
- [ ] Regression testing
- [ ] Coverage basics

### 32. Secure Code Analysis
- [ ] Reading unfamiliar code
- [ ] Tracing user input through an application
- [ ] Identifying trust boundaries
- [ ] Finding missing authorization checks
- [ ] Reviewing database queries
- [ ] Identifying hardcoded secrets
- [ ] Reviewing file operations
- [ ] Reviewing subprocess calls
- [ ] Understanding static-analysis findings
- [ ] Recognizing false positives
- [ ] Remediation and verification

### 33. Code Quality and Performance
- [ ] PEP 8
- [ ] Readable naming and function design
- [ ] Type hints
- [ ] `dataclasses`
- [ ] Basic design principles
- [ ] Refactoring
- [ ] Profiling basics
- [ ] Efficient file processing
- [ ] Memory usage
- [ ] Dependency pinning
- [ ] Reproducible environments

---

## Phase 8: Advanced Python Topics

Study these after you are comfortable with the earlier phases.

### 34. Advanced Language Features
- [ ] Decorators
- [ ] Context managers
- [ ] Custom iterators
- [ ] Advanced generators
- [ ] Closures
- [ ] Descriptors (introductory understanding)
- [ ] Advanced class design
- [ ] Metaclasses (optional)
- [ ] Structural pattern matching
- [ ] Advanced typing
- [ ] Protocols and generics
- [ ] Functional programming concepts

### 35. Concurrency and Asynchronous Programming
- [ ] `threading`
- [ ] `multiprocessing`
- [ ] `concurrent.futures`
- [ ] `asyncio`
- [ ] Async functions and `await`
- [ ] Async HTTP clients
- [ ] Concurrency limitations
- [ ] Timeouts and cancellation
- [ ] Race conditions
- [ ] Resource management

### 36. Cryptography Fundamentals
- [ ] Encoding vs. encryption vs. hashing
- [ ] Symmetric encryption
- [ ] Asymmetric encryption
- [ ] Digital signatures
- [ ] Message authentication codes
- [ ] Secure random values
- [ ] Password hashing and salts
- [ ] Key management
- [ ] TLS concepts
- [ ] Using established cryptographic libraries
- [ ] Common cryptographic implementation mistakes

### 37. Python Internals and Runtime
- [ ] Python execution model
- [ ] Namespaces and object references
- [ ] Garbage collection basics
- [ ] Bytecode concepts
- [ ] Import system
- [ ] Dependency and package security
- [ ] Virtual environments
- [ ] Python runtime security considerations

---

## Phase 9: Python Security Projects

Build these projects as you learn the relevant topics.

### Beginner Projects
- [ ] File-integrity checker using hashes
- [ ] Authentication-log analyser
- [ ] Failed-login counter
- [ ] Directory and file inventory tool
- [ ] JSON and CSV security-report processor

### Intermediate Projects
- [ ] HTTP response and security-header checker for authorized targets
- [ ] Python API client for your own test application
- [ ] Web access-log analyser
- [ ] Command-line security reporting tool
- [ ] File-upload validation test suite
- [ ] Authentication and authorization regression tests

### Application Security Projects
- [ ] Secure Flask, Django, or FastAPI application
- [ ] Role-based authorization implementation
- [ ] Automated security regression tests
- [ ] Dependency and secret-scanning workflow
- [ ] Static-analysis integration
- [ ] CI/CD security checks
- [ ] Security code-review report
- [ ] Threat model for a web application

### Advanced Projects
- [ ] Modular Python security toolkit for a controlled lab
- [ ] Automated log-analysis and alerting pipeline
- [ ] API security test suite for your own application
- [ ] Secure development pipeline with documented findings
- [ ] Vulnerable-versus-fixed application demonstrating remediation

---

## Recommended Learning Priority

### Must Know First
1. Python fundamentals
2. Functions and data structures
3. Files and exceptions
4. Modules and virtual environments
5. Regular expressions
6. Command-line arguments
7. Python HTTP programming
8. JSON and API interaction
9. Python logging
10. Bash and Linux integration

### Learn Alongside Web Security
1. Networking with Python
2. HTML parsing and URL handling
3. Database programming
4. Secure coding
5. Automated testing
6. Code review
7. Web framework security

### Learn Later
1. Advanced OOP
2. Concurrency and asynchronous programming
3. Advanced typing
4. Python internals
5. Advanced cryptographic APIs
6. Complex design patterns

---

## Final Goal

By the end of this roadmap, aim to be able to:

- Write useful Python automation without relying entirely on tutorials.
- Build and test small HTTP clients and API tools.
- Analyse logs and structured security data.
- Use Bash to automate Linux workflows.
- Read web application code and recognize security weaknesses.
- Implement and test secure application features.
- Build a useful security project with documentation and automated tests.
- Explain your findings clearly in a technical report.

**Remember:** You do not need to finish every advanced Python topic before learning web security. Learn the foundations first, then study new Python concepts when your security labs and projects require them.
