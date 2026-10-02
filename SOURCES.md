# Source ledger

Reviewed 2026-10-02. These are primary publications maintained by their issuing organizations. They anchor proposed research; a citation does not validate a proposed design, establish compliance, or prove a result. Source versions and machine-readable data should be pinned when a concept advances to implementation.

| ID | Primary source | What it supports | Scope and caveat |
|---|---|---|---|
| S01 | [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) | Govern, Identify, Protect, Detect, Respond, Recover outcomes and profiles. | Published 2024; outcome taxonomy, not an implementation checklist. |
| S02 | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Security and privacy control families. | Final 2020 with later release updates; controls require tailoring. |
| S03 | [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) | Assessment plans and evidence procedures. | Final 2022, updated releases; passing a prototype check is not certification. |
| S04 | [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Resource-centered, continuously evaluated access. | Architecture guidance, not a product or guarantee. |
| S05 | [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final) | Service-identity policy across cloud applications. | Final 2023; requires local threat and deployment model. |
| S06 | [NIST SP 800-63 Rev. 4](https://pages.nist.gov/800-63-4/) | Digital identity assurance, proofing, authentication, federation, and usability. | Final July 2025; human identity scope does not directly specify machine identity. |
| S07 | [CISA, Shifting the Balance of Cybersecurity Risk](https://www.cisa.gov/sites/default/files/2023-10/Shifting-the-Balance-of-Cybersecurity-Risk-Principles-and-Approaches-for-Secure-by-Design-Software.pdf) | Secure design and default settings; manufacturer ownership of customer outcomes. | Multi-agency guidance; no specific implementation conformance claim. |
| S08 | [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure-development practices across the lifecycle. | Final 2022; adapt tasks to each development environment. |
| S09 | [CISA, Minimum Elements for an SBOM](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf) | Version-specific component relationships and dependency visibility. | August 2025; an SBOM alone does not prove absence of vulnerabilities. |
| S10 | [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) | Source/build provenance and graduated assurance. | Approved specification; level claims require actual evidence. |
| S11 | [Sigstore documentation](https://docs.sigstore.dev/) | Identity-bound signatures and transparency-log verification. | Transparency records signatures, not functional correctness. |
| S12 | [OpenSSF Scorecard](https://openssf.org/scorecard/) | Automated indicators of open-source project security practices. | Risk signal, not an absolute trust score. |
| S13 | [OWASP ASVS 5.0](https://owasp.org/projects/asvs?tab=main) | Versioned application-security verification requirements. | Pin requirement IDs to v5.0.0 when citing individual checks. |
| S14 | [OWASP API Security Top 10: 2023](https://api-security.owasp.org/editions/2023/en/0x00-header/) | API authorization, resource, inventory, and business-flow risks. | Awareness taxonomy; not exhaustive test coverage. |
| S15 | [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Evidence of exploitation in the wild for prioritization. | Live catalog; snapshot date required for reproducible analysis. |
| S16 | [MITRE ATT&CK Enterprise tactics](https://attack.mitre.org/tactics/) | Adversary objectives and technique mapping. | Evolving knowledge base, not prevalence statistics. |
| S17 | [MITRE D3FEND knowledge graph](https://d3fend.mitre.org/about/) | Defensive mechanisms and their relationships to artifacts and threats. | Countermeasure ontology, not proof that a product works. |
| S18 | [OASIS STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/) | Structured threat-intelligence exchange. | Schema validity and source credibility are separate concerns. |
| S19 | [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) | Current EU incident and dependency trends. | Published September 2026, observing 2025; trends need not generalize globally. |
| S20 | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Incident response integrated into CSF 2.0 risk management. | Final 2025; local playbooks still required. |
| S21 | [NIST IR 8374 Rev. 1](https://csrc.nist.gov/pubs/ir/8374/r1/final) | Ransomware risk and recovery profile. | Final June 2026; supersedes the original IR 8374. |
| S22 | [Kubernetes security concepts](https://kubernetes.io/docs/concepts/security/) | Cluster/API protection, audit and workload policy. | Implementation details are version-dependent. |
| S23 | [SPIFFE overview](https://spiffe.io/docs/latest/spiffe-about/overview/) | Attested, short-lived workload identities. | Identity issuance does not by itself decide authorization. |
| S24 | [NIST SP 800-82 Rev. 3, OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Security with industrial safety, reliability and availability constraints. | Final 2023; Rev. 4 is only a draft as of review. |
| S25 | [NIST SP 800-213, IoT Device Cybersecurity](https://csrc.nist.gov/pubs/sp/800/213/final) | Acquirer/manufacturer device requirements. | Final 2021; revisions in development as of review. |
| S26 | [NASA Space Security Best Practices Guide](https://swehb.nasa.gov/spaces/SWEHBVD/pages/146540183/7.22%2B-%2BSpace%2BSecurity%2BBest%2BPractices%2BGuide) | Spacecraft and ground-segment mission security principles. | Mission-specific control tailoring remains necessary. |
| S27 | [NIST IR 8401, Satellite Ground Segment Profile](https://www.nist.gov/publications/satellite-ground-segment-applying-cybersecurity-framework-satellite-command-and-control) | Command/control ground-segment cybersecurity profile. | Published 2022; focus is operational ground segment. |
| S28 | [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) | Govern, Map, Measure and Manage AI risks. | Voluntary 2023 framework; revision underway as of review. |
| S29 | [NIST Generative AI Profile, AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Generative-AI risk management across the lifecycle. | Cross-sector profile, not a certification or model benchmark. |
| S30 | [CISA and UK NCSC, Secure AI System Development](https://www.cisa.gov/news-events/alerts/2023/11/26/cisa-and-uk-ncsc-unveil-joint-guidelines-secure-ai-system-development) | Secure design, model development, deployment and operation. | Guidance applies to AI systems; local evaluation remains essential. |
| S31 | [NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) | ML-KEM key establishment. | Final 2024; deployment needs protocol and key-lifecycle analysis. |
| S32 | [NIST FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) | ML-DSA digital signatures. | Final 2024; NIST lists potential minor errata. |
| S33 | [NIST FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) | SLH-DSA digital signatures. | Final 2024; performance may constrain embedded use. |
| S34 | [NIST CSWP 39 update 1, Crypto Agility](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final) | Algorithm replacement and interoperability planning. | Updated June 2026; no universal migration schedule. |
| S35 | [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Enterprise privacy-risk management. | Current published framework is 1.0; 1.1 is an initial public draft as of review. |
| S36 | [NIST SP 800-226, Differential Privacy](https://csrc.nist.gov/pubs/sp/800/226/final) | Quantifiable privacy loss and implementation pitfalls. | Final 2025; formal guarantees depend on correct accounting and deployment. |

## Additional references cited by the idea chapters

The entries below close the URL ledger over all 150 ideas. Several are more specific pages of a source already above; they remain separate entries so a reader can audit the exact destination used in an idea. The reference's scope matters: a standards page provides design guidance, not evidence that the proposed concept works.

### Systems architecture and risk governance

| ID | Primary source | Scope and limitation |
|---|---|---|
| S43 | [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) | Current final systems security engineering publication (2022); applies trustworthy-system principles across the lifecycle, not a proof of a given design. |
| S44 | [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) | Final cyber-resilient systems engineering approach (2021); model resilience objectives and tradeoffs locally. |
| S66 | [NIST Cybersecurity Framework resource center](https://www.nist.gov/cyberframework) | Current CSF resources and profiles; landing page may change, while S01 pins the CSF 2.0 publication. |
| S67 | [NIST CSF 2.0 Profiles](https://www.nist.gov/cyberframework/profiles) | Tailoring and documenting target/current outcomes; a profile does not certify implementation. |
| S69 | [NIST, Engineering Trustworthy Secure Systems](https://www.nist.gov/publications/engineering-trustworthy-secure-systems) | Publication landing page for SP 800-160 Vol. 1 Rev. 1; same publication as S43, not an independent source. |

### Application, PCB, firmware and device trust

| ID | Primary source | Scope and limitation |
|---|---|---|
| S37 | [OWASP API Security Top 10 risk list](https://api-security.owasp.org/editions/2023/en/0x11-t10/) | Direct 2023 risk-list page; awareness categories are not exhaustive tests. |
| S38 | [OWASP API4:2023, Unrestricted Resource Consumption](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/) | Specific API resource-consumption risk; no numerical service limit is prescribed for every system. |
| S41 | [NIST SP 1800-34, Validating the Integrity of Computing Devices](https://csrc.nist.gov/pubs/sp/1800/34/final) | Final 2022 example approach for device-integrity validation; a practice guide is not a universal hardware certification. |
| S48 | [NIST SP 800-193, Platform Firmware Resiliency](https://csrc.nist.gov/pubs/sp/800/193/final) | Protect, detect and recover firmware state; published 2018, still a design guide. |
| S56 | [MITRE CWE-20, Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html) | Weakness definition useful for requirements traceability; a CWE association does not identify an exploit. |
| S57 | [KiCad 9.0 PCB Editor documentation](https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html) | Primary CAD instructions for board design and DRC; software-version-specific, not electrical design approval. |
| S58 | [OpenTitan secure hardware design guidelines](https://opentitan.org/book/doc/security/implementation_guidelines/hardware/index.html) | OpenTitan project's published design practices; adapt before reuse on another chip. |
| S59 | [OpenTitan device life cycle](https://opentitan.org/book/doc/security/specs/device_life_cycle/) | Project-specific secure states and transitions; not a general standard. |
| S60 | [OpenTitan AES theory of operation](https://opentitan.org/book/hw/ip/aes/doc/theory_of_operation.html) | Concrete accelerator design example; not proof that a derivative implementation is side-channel safe. |
| S61 | [OpenTitan key-manager hardware interfaces](https://opentitan.org/book/hw/ip/keymgr/doc/interfaces.html) | Project-specific key-manager interfaces; cite as an architectural example, not a universal pinout. |
| S63 | [Trusted Computing Group TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/) | Issuer's TPM specification and versions; hardware assurance depends on implementation and validation. |

### Manufacturing and software supply-chain evidence

| ID | Primary source | Scope and limitation |
|---|---|---|
| S39 | [NIST IR 8536, Supply Chain Traceability](https://csrc.nist.gov/pubs/ir/8536/final) | Final September 2026 manufacturing traceability meta-framework; provenance records need independent verification. |
| S40 | [NIST SP 1326, C-SCRM Due Diligence Quick-Start Guide](https://csrc.nist.gov/pubs/sp/1326/final) | Final July 2026 supplier/product due-diligence guidance; not a supplier endorsement. |
| S45 | [NIST SP 800-161 Rev. 1, update 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) | Current final C-SCRM guidance (2022 publication, updated 2024); the earlier `/r1/final` page is withdrawn. |
| S68 | [NIST Digital Thread for Manufacturing](https://www.nist.gov/programs-projects/digital-thread-manufacturing) | Primary research program for lifecycle manufacturing data connection; contextual basis, not a cybersecurity assurance standard. |

### Network observability, configuration and threat sharing

| ID | Primary source | Scope and limitation |
|---|---|---|
| S42 | [NIST SP 800-150, Cyber Threat Information Sharing](https://csrc.nist.gov/pubs/sp/800/150/final) | Guidance on useful, timely and appropriate information sharing; permissions and quality controls remain local. |
| S49 | [NIST SP 800-215, Secure Enterprise Network Landscape](https://csrc.nist.gov/pubs/sp/800/215/final) | Final 2022 network architecture guidance; cannot validate a specific topology. |
| S70 | [IETF RFC 4035, DNSSEC protocol modifications](https://www.rfc-editor.org/info/rfc4035/) | Normative DNSSEC validation behavior; check current errata and updates for deployments. |
| S71 | [IETF RFC 6241, NETCONF](https://www.rfc-editor.org/info/rfc6241/) | Normative network-configuration protocol; authorization and device-specific support still matter. |
| S72 | [IETF RFC 7011, IPFIX](https://www.rfc-editor.org/info/rfc7011/) | Normative flow-export format; records describe observation, not every packet. |
| S73 | [IETF RFC 8915, Network Time Security](https://www.rfc-editor.org/info/rfc8915/) | Authenticated NTP time synchronization; correct deployment and trusted clocks remain necessary. |
| S74 | [IETF RFC 9232, Network Telemetry Framework](https://www.rfc-editor.org/info/rfc9232/) | Telemetry architecture and terminology; collection coverage must be measured. |

### Space systems and ground operations

| ID | Primary source | Scope and limitation |
|---|---|---|
| S62 | [NASA-STD-1006A, Space System Protection Standard](https://standards.nasa.gov/standard/nasa/nasa-std-1006) | Active NASA standard; its mandatory applicability is to NASA programs/projects, not every external mission. |
| S65 | [NASA SmallSat Ground Data Systems and Mission Operations](https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/) | NASA technical context for ground-system architecture; not a cybersecurity standard by itself. |

### Workforce, response and authorized exposure management

| ID | Primary source | Scope and limitation |
|---|---|---|
| S46 | [NIST SP 800-181 Rev. 1, NICE Workforce Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final) | Cybersecurity work roles and competencies; not an individual's qualification certificate. |
| S50 | [NIST SP 800-216, Federal Vulnerability Disclosure Guidelines](https://csrc.nist.gov/pubs/sp/800/216/final) | Coordinated disclosure processes for federal systems; no authorization to probe a system is implied. |
| S51 | [NIST SP 800-34 Rev. 1, update 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | Contingency planning (2010); adapt to current infrastructure and business impact. |
| S52 | [NIST SP 800-40 Rev. 4, Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final) | Patch-planning framework; timing depends on asset, exploit, safety and operations. |
| S53 | [NIST SP 800-50 Rev. 1, Cybersecurity and Privacy Learning](https://csrc.nist.gov/pubs/sp/800/50/r1/final) | Final 2024 program design guidance; learning outcomes require measurement. |
| S64 | [CISA BOD 23-01, Asset Visibility and Vulnerability Detection](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks) | Federal civilian executive branch directive; scope excludes ephemeral assets and does not generally bind non-federal entities. |

### Privacy, measurement and evaluation

| ID | Primary source | Scope and limitation |
|---|---|---|
| S47 | [NIST SP 800-188, De-Identifying Government Datasets](https://csrc.nist.gov/pubs/sp/800/188/final) | De-identification techniques and governance; residual re-identification risk remains. |
| S54 | [NIST SP 800-55 Vol. 1, Identifying and Selecting Measures](https://csrc.nist.gov/pubs/sp/800/55/v1/final) | Final 2024 measure selection; chosen indicators need construct validity. |
| S55 | [NIST SP 800-55 Vol. 2, Measurement Program](https://csrc.nist.gov/pubs/sp/800/55/v2/final) | Final 2024 measurement-program design; metrics do not automatically show causal security improvement. |

All ideas in `atlas/` are research proposals. “Data” means a named, authorized input or a synthetic test fixture until acquisition is documented; no uploaded user artifact is included or re-published here.
