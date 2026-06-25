A01:2025 Broken Access Control
Background.
Maintaining its position at #1 in the Top Ten, 100% of the applications tested were found to have some form of broken access control. Notable CWEs included are CWE-200: Exposure of Sensitive Information to an Unauthorized Actor, CWE-201: Exposure of Sensitive Information Through Sent Data, CWE-918 Server-Side Request Forgery (SSRF), and CWE-352: Cross-Site Request Forgery (CSRF). This category has the highest number of occurrences in the contributed data, and second highest number of related CVEs.
Description.
Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside the user's limits. Common access control vulnerabilities include:

Violation of the principle of least privilege, commonly known as deny by default, where access should only be granted for particular capabilities, roles, or users, but is available to anyone.
Bypassing access control checks by modifying the URL (parameter tampering or force browsing), internal application state, or the HTML page, or by using an attack tool that modifies API requests.
Permitting viewing or editing someone else's account by providing its unique identifier (insecure direct object references)
An accessible API with missing access controls for POST, PUT, and DELETE.
Elevation of privilege. Acting as a user without being logged in or or gaining privileges beyond those expected of the logged in user (e.g. admin access).
Metadata manipulation, such as replaying or tampering with a JSON Web Token (JWT) access control token, a cookie or hidden field manipulated to elevate privileges, or abusing JWT invalidation.
CORS misconfiguration allows API access from unauthorized or untrusted origins.
Force browsing (guessing URLs) to authenticated pages as an unauthenticated user or to privileged pages as a standard user.
How to prevent.
Access control is only effective when implemented in trusted server-side code or serverless APIs, where the attacker cannot modify the access control check or metadata.

Except for public resources, deny by default.
Implement access control mechanisms once and reuse them throughout the application, including minimizing Cross-Origin Resource Sharing (CORS) usage.
Model access controls should enforce record ownership rather than allowing users to create, read, update, or delete any record.
Unique application business limit requirements should be enforced by domain models.
Disable web server directory listing and ensure file metadata (e.g., .git) and backup files are not present within web roots.
Log access control failures, alert admins when appropriate (e.g., repeated failures).
Implement rate limits on API and controller access to minimize the harm from automated attack tooling.
Stateful session identifiers should be invalidated on the server after logout. Stateless JWT tokens should be short-lived to minimize the window of opportunity for an attacker. For longer-lived JWTs, consider using refresh tokens and following OAuth standards to revoke access.
Use well-established toolkits or patterns that provide simple, declarative access controls.
Developers and QA staff should include functional access control in their unit and integration tests.

Example attack scenarios.
Scenario #1: The application uses unverified data in an SQL call that is accessing account information:

pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery( );
An attacker can simply modify the browser's 'acct' parameter to send any desired account number. If not correctly verified, the attacker can access any user's account.

https://example.com/app/accountInfo?acct=notmyacct
Scenario #2: An attacker simply forces browsers to target URLs. Admin rights are required for access to the admin page.

https://example.com/app/getappInfo
https://example.com/app/admin_getappInfo
If an unauthenticated user can access either page, it's a flaw. If a non-admin can access the admin page, this is a flaw.

Scenario #3: An application puts all of their access control in their front-end. While the attacker cannot get to https://example.com/app/admin_getappInfo due to JavaScript code running in the browser, they can simply execute:

$ curl https://example.com/app/admin_getappInfo
from the command line.


A02:2025 Security Misconfigurationicon
Background.
Moving up from #5 in the previous edition, 100% of the applications tested were found to have some form of misconfiguration, with an average incidence rate of 3.00%, and over 719k occurrences of a Common Weakness Enumeration (CWE) in this risk category. With more shifts into highly configurable software, it's not surprising to see this category moving up. Notable CWEs included are CWE-16 Configuration and CWE-611 Improper Restriction of XML External Entity Reference (XXE).

Score table.
CWEs Mapped	Max Incidence Rate	Avg Incidence Rate	Max Coverage	Avg Coverage	Avg Weighted Exploit	Avg Weighted Impact	Total Occurrences	Total CVEs
16	27.70%	3.00%	100.00%	52.35%	7.96	3.97	719,084	1,375
Description.
Security misconfiguration is when a system, application, or cloud service is set up incorrectly from a security perspective, creating vulnerabilities.

The application might be vulnerable if:

It is missing appropriate security hardening across any part of the application stack or improperly configured permissions on cloud services.
Unnecessary features are enabled or installed (e.g., unnecessary ports, services, pages, accounts, testing frameworks, or privileges).
Default accounts and their passwords are still enabled and unchanged.
A lack of central configuration for intercepting excessive error messages. Error handling reveals stack traces or other overly informative error messages to users.
For upgraded systems, the latest security features are disabled or not configured securely.
Excessive prioritization of backward compatibility leading to insecure configuration.
The security settings in the application servers, application frameworks (e.g., Struts, Spring, ASP.NET), libraries, databases, etc., are not set to secure values.
The server does not send security headers or directives, or they are not set to secure values.
Without a concerted, repeatable application security configuration hardening process, systems are at a higher risk.

How to prevent.
Secure installation processes should be implemented, including:

A repeatable hardening process enabling the fast and easy deployment of another environment that is appropriately locked down. Development, QA, and production environments should all be configured identically, with different credentials used in each environment. This process should be automated to minimize the effort required to set up a new secure environment.
A minimal platform without any unnecessary features, components, documentation, or samples. Remove or do not install unused features and frameworks.
A task to review and update the configurations appropriate to all security notes, updates, and patches as part of the patch management process (see A03 Software Supply Chain Failures). Review cloud storage permissions (e.g., S3 bucket permissions).
A segmented application architecture provides effective and secure separation between components or tenants, with segmentation, containerization, or cloud security groups (ACLs).
Sending security directives to clients, e.g., Security Headers.
An automated process to verify the effectiveness of the configurations and settings in all environments.
Proactively add a central configuration to intercept excessive error messages as a backup.
If these verifications are not automated, they should be manually verified annually at a minimum.
Use identity federation, short-lived credentials, or role-based access mechanisms provided by the underlying platform instead of embedding static keys or secrets in code, configuration files, or pipelines.
Example attack scenarios.
Scenario #1: The application server comes with sample applications not removed from the production server. These sample applications have known security flaws that attackers use to compromise the server. Suppose one of these applications is the admin console, and default accounts weren't changed. In that case, the attacker logs in with the default password and takes over.

Scenario #2: Directory listing is not disabled on the server. An attacker discovers they can simply list directories. The attacker finds and downloads the compiled Java classes, which they decompile and reverse engineer to view the code. The attacker then finds a severe access control flaw in the application.

Scenario #3: The application server's configuration allows detailed error messages, such as stack traces to be returned to users. This potentially exposes sensitive information or underlying flaws, such as component versions that are known to be vulnerable.

Scenario #4: A cloud service provider (CSP) defaults to having sharing permissions open to the Internet. This allows sensitive data stored within cloud storage to be accessed.

A03:2025 Software Supply Chain Failuresicon
Background.
This was top-ranked in the Top 10 community survey with exactly 50% respondents ranking it #1. Since initially appearing in the 2013 Top 10 as "A9 – Using Components with Known Vulnerabilities", the risk has grown in scope to include all supply chain failures, not just ones involving known vulnerabilities. Despite this increased scope, supply chain failures continue to be a challenge to identify with only 11 Common Vulnerability and Exposures (CVEs) having the related CWEs. However, when tested and reported in the contributed data, this category has the highest average incidence rate at 5.19%. The relevant CWEs are CWE-477: Use of Obsolete Function, CWE-1104: Use of Unmaintained Third Party Components, CWE-1329: Reliance on Component That is Not Updateable, and CWE-1395: Dependency on Vulnerable Third-Party Component.

Score table.
CWEs Mapped	Max Incidence Rate	Avg Incidence Rate	Max Coverage	Avg Coverage	Avg Weighted Exploit	Avg Weighted Impact	Total Occurrences	Total CVEs
6	9.56%	5.72%	65.42%	27.47%	8.17	5.23	215,248	11
Description.
Software supply chain failures are breakdowns or other compromises in the process of building, distributing, or updating software. They are often caused by vulnerabilities or malicious changes in third-party code, tools, or other dependencies that the system relies on.

You are likely vulnerable if:

you do not carefully track the versions of all components that you use (both client-side and server-side). This includes components you directly use as well as nested (transitive) dependencies.
the software is vulnerable, unsupported, or out of date. This includes the OS, web/application server, database management system (DBMS), applications, APIs and all components, runtime environments, and libraries.
you do not scan for vulnerabilities regularly and subscribe to security bulletins related to the components you use.
you do not have a change management process or tracking of changes within your supply chain, including tracking IDEs, IDE extensions and updates, changes to your organization's code repository, sandboxes, image and library repositories, the way artifacts are created and stored, etc. Every part of your supply chain should be documented, especially changes.
you have not hardened every part of your supply chain, with a special focus on access control and the application of least privilege.
your supply chain systems do not have any separation of duty. No single person should be able to write code and promote it all the way to production without oversight from another human being.
components from untrusted sources, across any part of the tech stack, are used in or can impact on production environments.
you do not fix or upgrade the underlying platform, frameworks, and dependencies in a risk-based, timely fashion. This commonly happens in environments when patching is a monthly or quarterly task under change control, leaving organizations open to days or months of unnecessary exposure before fixing vulnerabilities.
software developers do not test the compatibility of updated, upgraded, or patched libraries.
you do not secure the configurations of every part of your system (see A02:2025-Security Misconfiguration).
your CI/CD pipeline has weaker security than the systems it builds and deploys, especially if it is complex.
How to prevent.
There should be a patch management process in place to:

Centrally generate and manage the Software Bill of Materials (SBOM) of your entire software.
Track not just your direct dependencies, but their (transitive) dependencies, and so on.
Reduce attack surface by removing unused dependencies, unnecessary features, components, files, and documentation.
Continuously inventory the versions of both client-side and server-side components (e.g., frameworks, libraries) and their dependencies using tools like OWASP Dependency Track, OWASP Dependency Check, retire.js, etc.
Continuously monitor sources like Common Vulnerability and Exposures (CVE), National Vulnerability Database (NVD), and Open Source Vulnerabilities (OSV) for vulnerabilities in the components you use. Use software composition analysis, software supply chain, or security-focused SBOM tools to automate the process. Subscribe to alerts for security vulnerabilities related to components you use.
Only obtain components from official (trusted) sources over secure links. Prefer signed packages to reduce the chance of including a modified, malicious component (see A08:2025-Software and Data Integrity Failures).
Deliberately choose which version of a dependency you use and upgrade only when there is need.
Monitor for libraries and components that are unmaintained or do not create security patches for older versions. If patching is not possible, consider migrating to an alternative. If that is not possible, consider deploying a virtual patch to monitor, detect, or protect against the discovered issue.
Update your CI/CD, IDE, and any other developer tooling regularly
Avoid deploying updates to all systems simultaneously. Use staged rollouts or canary deployments to limit exposure in case a trusted vendor is compromised.
There should be a change management process or tracking system in place to track changes to:

CI/CD settings (all build tools and pipelines)
Code repositories
Sandbox areas
Developer IDEs
SBOM tooling, and created artifacts
Logging systems and logs
Third party integrations, such as SaaS
Artifact repositories
Container registries
Harden the following systems, which includes enabling MFA and locking down IAM:

Your code repository (which includes not checking in secrets, protecting branches, backups)
Developer workstations (regular patching, MFA, monitoring, and more)
Your build server & CI/CD (separation of duties, access control, signed builds, environment-scoped secrets, tamper-evident logs, more)
Your artifacts (ensure integrity via provenance, signing, and time stamping, promote artifacts rather than rebuilding for each environment, ensure builds are immutable)
Infrastructure as code (managed like all code, including use of PRs and version control)
Every organization must ensure an ongoing plan for monitoring, triaging, and applying updates or configuration changes for the lifetime of the application or portfolio.

Example attack scenarios.
Scenario #1: A trusted vendor is compromised with malware, leading to your computer systems being compromised when you upgrade. The most famous example of this is probably:

The 2019 SolarWinds compromise that led to ~18,000 organizations being compromised. https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack
Scenario #2: A trusted vendor is compromised such that it behaves maliciously only under a specific condition.

The 2025 Bybit theft of $1.5 billion was caused by a supply chain attack in wallet software that only executed when the target wallet was being used.
Scenario #3: The Shai-Hulud supply chain attack in 2025 was the first successful self-propagating npm worm. Attacks seeded malicious versions of popular packages, which used a post-install script to harvest and exfiltrate sensitive data to public GitHub repositories. The malware would also detect npm tokens in the victim environment, and automatically use them to push malicious versions of any accessible package. The worm reached over 500 package versions before being disrupted by npm. This supply chain attack was advanced, fast-spreading, and damaging, and by targeting developer machines it demonstrated developers themselves are now prime targets for supply chain attacks.

Scenario #4: Components typically run with the same privileges as the application itself, so flaws in any component can result in serious impact. Such flaws can be accidental (e.g., coding error) or intentional (e.g., a backdoor in a component). Some example exploitable component vulnerabilities discovered are:

CVE-2017-5638, a Struts 2 remote code execution vulnerability that enables the execution of arbitrary code on the server, has been blamed for significant breaches.
CVE-2021-44228 ("Log4Shell"), an Apache Log4j remote code execution zero-day vulnerability, has been blamed for ransomware, cryptomining, and other attack campaigns.

A04:2025 Cryptographic Failuresicon
Background.
Moving down two positions to #4, this weakness focuses on failures related to the lack of cryptography, insufficiently strong cryptography, leaking of cryptographic keys, and related errors. Three of the most common Common Weakness Enumerations (CWEs) in this risk involved the use of a weak pseudo-random number generator: CWE-327 Use of a Broken or Risky Cryptographic Algorithm, CWE-331: Insufficient Entropy, CWE-1241: Use of Predictable Algorithm in Random Number Generator, and CWE-338 Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG).

Score table.
CWEs Mapped	Max Incidence Rate	Avg Incidence Rate	Max Coverage	Avg Coverage	Avg Weighted Exploit	Avg Weighted Impact	Total Occurrences	Total CVEs
32	13.77%	3.80%	100.00%	47.74%	7.23	3.90	1,665,348	2,185
Description.
Generally speaking, all data in transit should be encrypted at the transport layer (OSI layer 4). Previous hurdles such as CPU performance and private key/certificate management are now handled by CPUs having instructions designed to accelerate encryption (eg: AES support) and private key and certificate management being simplified by services like LetsEncrypt.org with major cloud vendors providing even more tightly integrated certificate management services for their specific platforms.

Beyond securing the transport layer, it is important to determine what data needs encryption at rest as well as what data needs extra encryption in transit (at the application layer, OSI layer 7). For example, passwords, credit card numbers, health records, personal information, and business secrets require extra protection, especially if that data falls under privacy laws, e.g., EU's General Data Protection Regulation (GDPR), or regulations such as PCI Data Security Standard (PCI DSS). For all such data:

Are any old or weak cryptographic algorithms or protocols used either by default or in older code?
Are default crypto keys in use, are weak crypto keys generated, are keys re-used, or is proper key management and rotation missing?
Are crypto keys checked into source code repositories?
Is encryption not enforced, e.g., are any HTTP headers (browser) security directives or headers missing?
Is the received server certificate and the trust chain properly validated?
Are initialization vectors ignored, reused, or not generated sufficiently secure for the cryptographic mode of operation? Is an insecure mode of operation such as ECB in use? Is encryption used when authenticated encryption is more appropriate?
Are passwords being used as cryptographic keys in the absence of a password based key derivation function?
Is randomness used that was not designed to meet cryptographic requirements? Even if the correct function is chosen, does it need to be seeded by the developer, and if not, has the developer over-written the strong seeding functionality built into it with a seed that lacks sufficient entropy/unpredictability?
Are deprecated hash functions such as MD5 or SHA1 in use, or are non-cryptographic hash functions used when cryptographic hash functions are needed?
Are cryptographic error messages or side channel information exploitable, for example in the form of padding oracle attacks?
Can the cryptographic algorithm be downgraded or bypassed?
See references ASVS: Cryptography (V11), Secure Communication (V12) and Data Protection (V14).

How to prevent.
Do the following, at a minimum, and consult the references:

Classify and label data processed, stored, or transmitted by an application. Identify which data is sensitive according to privacy laws, regulatory requirements, or business needs.
Store your most sensitive keys in a hardware or cloud-based HSM.
Use well-trusted implementations of cryptographic algorithms whenever possible.
Don't store sensitive data unnecessarily. Discard it as soon as possible or use PCI DSS compliant tokenization or even truncation. Data that is not retained cannot be stolen.
Make sure to encrypt all sensitive data at rest.
Ensure up-to-date and strong standard algorithms, protocols, and keys are in place; use proper key management.
Encrypt all data in transit with protocols >= TLS 1.2 only, with forward secrecy (FS) ciphers, drop support for cipher block chaining (CBC) ciphers, support quantum key change algorithms. For HTTPS enforce encryption using HTTP Strict Transport Security (HSTS). Check everything with a tool.
Disable caching for responses that contain sensitive data. This includes caching in your CDN, web server, and any application caching (eg: Redis).
Apply required security controls as per the data classification.
Do not use unencrypted protocols such as FTP, and STARTTLS. Avoid using SMTP for transmitting confidential data.
Store passwords using strong adaptive and salted hashing functions with a work factor (delay factor), such as Argon2, yescrypt, scrypt or PBKDF2-HMAC-SHA-512. For legacy systems using bcrypt, get more advice at OWASP Cheat Sheet: Password Storage
Initialization vectors must be chosen appropriate for the mode of operation. This could mean using a CSPRNG (cryptographically secure pseudo random number generator). For modes that require a nonce, the initialization vector (IV) does not need a CSPRNG. In all cases, the IV should never be used twice for a fixed key.
Always use authenticated encryption instead of just encryption.
Keys should be generated cryptographically randomly and stored in memory as byte arrays. If a password is used, then it must be converted to a key via an appropriate password base key derivation function.
Ensure that cryptographic randomness is used where appropriate and that it has not been seeded in a predictable way or with low entropy. Most modern APIs do not require the developer to seed the CSPRNG to be secure.
Avoid deprecated cryptographic functions, block building methods and padding schemes, such as MD5, SHA1, Cipher Block Chaining Mode (CBC), PKCS number 1 v1.5.
Ensure settings and configurations meet security requirements by having them reviewed by security specialists, tools designed for this purpose, or both.
You need to prepare now for post quantum cryptography (PQC), see reference (ENISA) so that high risk systems are safe no later than the end of 2030.
Example attack scenarios.
Scenario #1: A site doesn't use or enforce TLS for all pages or supports weak encryption. An attacker monitors network traffic (e.g., at an insecure wireless network), downgrades connections from HTTPS to HTTP, intercepts requests, and steals the user's session cookie. The attacker then replays this cookie and hijacks the user's (authenticated) session, accessing or modifying the user's private data. Instead of the above they could alter all transported data, e.g., the recipient of a money transfer.

Scenario #2: The password database uses unsalted or simple hashes to store everyone's passwords. A file upload flaw allows an attacker to retrieve the password database. All the unsalted hashes can be exposed with a rainbow table of pre-calculated hashes. Hashes generated by simple or fast hash functions may be cracked by GPUs, even if they were salted.

A05:2025 Injectionicon
Background.
Injection falls two spots from #3 to #5 in the ranking, maintaining its position relative to A04:2025-Cryptographic Failures and A06:2025-Insecure Design. Injection is one of the most tested categories with 100% of applications tested for some form of injection. It had the greatest number of CVEs for any category, with 37 CWEs in this category. Injection includes Cross-site Scripting (high frequency/low impact) with more than 30k CVEs and SQL Injection (low frequency/high impact) with more than 14k CVEs. The massive number of reported CVEs for CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') brings down the average weighted impact of this category.

Score table.
CWEs Mapped	Max Incidence Rate	Avg Incidence Rate	Max Coverage	Avg Coverage	Avg Weighted Exploit	Avg Weighted Impact	Total Occurrences	Total CVEs
37	13.77%	3.08%	100.00%	42.93%	7.15	4.32	1,404,249	62,445
Description.
An injection vulnerability is an application flaw that allows untrusted user input to be sent to an interpreter (e.g. a browser, database, the command line) and causes the interpreter to execute parts of that input as commands.

An application is vulnerable to attack when:

User-supplied data is not validated, filtered, or sanitized by the application.
Dynamic queries or non-parameterized calls without context-aware escaping are used directly in the interpreter.
Unsanitized data is used within object-relational mapping (ORM) search parameters to extract additional, sensitive records.
Potentially hostile data is directly used or concatenated. The SQL or command contains the structure and malicious data in dynamic queries, commands, or stored procedures.
Some of the more common injections are SQL, NoSQL, OS command, Object Relational Mapping (ORM), LDAP, and Expression Language (EL) or Object Graph Navigation Library (OGNL) injection. The concept is identical among all interpreters. Detection is best achieved by a combination of source code review along with automated testing (including fuzzing) of all parameters, headers, URL, cookies, JSON, SOAP, and XML data inputs. The addition of static (SAST), dynamic (DAST), and interactive (IAST) application security testing tools into the CI/CD pipeline can also be helpful to identify injection flaws before production deployment.

A related class of injection vulnerabilities has become common in LLMs. These are discussed separately in the OWASP LLM Top 10, specifically LLM01:2025 Prompt Injection.

How to prevent.
The best means to prevent injection requires keeping data separate from commands and queries:

The preferred option is to use a safe API, which avoids using the interpreter entirely, provides a parameterized interface, or migrates to Object Relational Mapping Tools (ORMs). Note: Even when parameterized, stored procedures can still introduce SQL injection if PL/SQL or T-SQL concatenates queries and data or executes hostile data with EXECUTE IMMEDIATE or exec().
When it is not possible to separate the data from commands, you can reduce threats using the following techniques.

Use positive server-side input validation. This is not a complete defense as many applications require special characters, such as text areas or APIs for mobile applications.
For any residual dynamic queries, escape special characters using the specific escape syntax for that interpreter. Note: SQL structures such as table names, column names, and so on cannot be escaped, and thus user-supplied structure names are dangerous. This is a common issue in report-writing software.
Warning these techniques involve parsing and escaping complex strings, making them error-prone and not robust in the face of minor changes to the underlying system.

Example attack scenarios.
Scenario #1: An application uses untrusted data in the construction of the following vulnerable SQL call:

String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";
An attacker modifies the 'id' parameter value in their browser to send: ' OR '1'='1. For example:

http://example.com/app/accountView?id=' OR '1'='1
This changes the meaning of the query to return all records from the accounts table. More dangerous attacks could modify or delete data or even invoke stored procedures.

Scenario #2: An application's blind trust in frameworks may result in queries that are still vulnerable. For example, Hibernate Query Language (HQL):

Query HQLQuery = session.createQuery("FROM accounts WHERE custID='" + request.getParameter("id") + "'");
An attacker supplies: ' OR custID IS NOT NULL OR custID='. This bypasses the filter and returns all accounts. While HQL has fewer dangerous functions than raw SQL, it still allows unauthorized data access when user input is concatenated into queries.

Scenario #3: An application passes user input directly to an OS command:

String cmd = "nslookup " + request.getParameter("domain");
Runtime.getRuntime().exec(cmd);
An attacker supplies example.com; cat /etc/passwd to execute arbitrary commands on the server.