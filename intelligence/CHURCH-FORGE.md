# Church of Malware · Public forge source review

**Primary source:** [Explore repositories](https://git.churchofmalware.org/explore/repos), the URL selected by the user. **Reviewed:** 2026-10-03. **Evidence:** public publisher metadata.

The reviewed first Explore page displays 20 projects. The supplemental [Nightmare_Eclipse namespace](https://git.churchofmalware.org/Nightmare_Eclipse) displays 15; two overlap, yielding 33 distinct records. The primary listing is paginated: this is a bounded source review, not an exhaustive audit of the forge. Root-page access redirected to sign-in; the public listings were readable.

[Machine-readable catalog and source receipts](../data/intelligence/forge_catalog.json) · [Existing entity cards](README.md) · [Beginner tool guide](../foundations/TOOLS.md)

## Visible repository metadata

Categories are short analyst summaries of publisher descriptions. A missing or vague description remains insufficient information. The displayed update time is publisher metadata, not a release date, vulnerability discovery date or verified patch status. FG01 is Explore; FG02 is the namespace listing.

| Repository namespace/path | Description category | Displayed update (UTC) | Source |
|---|---|---|---|
| `K3ysTr0K3R/METIS` | Adversarial framework | 2026-10-03T15:42:12Z | FG01 |
| `K3ysTr0K3R/CVE-Exploits-Archive` | PoC collection | 2026-10-02T21:36:36Z | FG01 |
| `wh0crypt/8kto` | CPU emulator | 2026-09-30T22:59:17Z | FG01 |
| `ek0mssavi0r/solidSnake` | Insufficient description | 2026-09-30T07:14:09Z | FG01 |
| `Painter/FireFly_RK3326_R36MAX_R36S` | Communications project | 2026-09-29T23:47:36Z | FG01 |
| `leviathan/TRAMES` | Routing project | 2026-09-27T18:16:26Z | FG01 |
| `Painter/LaBuche-Stump` | Communications project | 2026-09-26T21:54:19Z | FG01 |
| `JYenn/EAsy` | Privilege-escalation claim | 2026-09-24T22:01:37Z | FG01 |
| `leviathan/OVERWATCH` | Insufficient description | 2026-09-22T05:02:51Z | FG01 |
| `mastercodeon/KsDumper-11` | Revival claim; insufficient detail | 2026-09-21T23:59:31Z | FG01 |
| `mastercodeon/VSAdminConfigurator` | Administrator-launch configuration | 2026-09-21T20:33:57Z | FG01 |
| `Nightmare_Eclipse/BigDiskBuster` | Endpoint-disruption claim | 2026-09-19T23:44:41Z | FG01, FG02 |
| `ek0mssavi0r/NIGHTSHADE_c4` | Adversarial framework | 2026-09-19T18:43:11Z | FG01 |
| `ek0mssavi0r/ek0msUSB` | Adversarial framework | 2026-09-19T17:09:55Z | FG01 |
| `ek0mssavi0r/Ranger-C3` | Command-and-control claim | 2026-09-19T17:03:48Z | FG01 |
| `Nightmare_Eclipse/ShieldCrash` | Endpoint-security claim | 2026-09-15T16:11:38Z | FG01, FG02 |
| `K3ysTr0K3R/MikroTik-Winbox-Scanner` | Network-fingerprinting claim | 2026-09-15T13:33:54Z | FG01 |
| `JYenn/Misery` | Credential-theft claim | 2026-09-14T23:17:04Z | FG01 |
| `ek0mssavi0r/swizBOT` | Adversarial framework | 2026-09-12T01:32:35Z | FG01 |
| `mastercodeon/TMOG-License-Patcher` | License-bypass claim | 2026-09-09T11:56:35Z | FG01 |
| `Nightmare_Eclipse/FalconFlank` | Endpoint-security claim | 2026-09-03T04:07:08Z | FG02 |
| `Nightmare_Eclipse/PrettyPrague` | Endpoint-security claim | 2026-08-30T16:50:09Z | FG02 |
| `Nightmare_Eclipse/HardBreacher` | Endpoint-security claim | 2026-08-29T03:02:15Z | FG02 |
| `Nightmare_Eclipse/ShieldBreak` | Endpoint-security claim | 2026-08-11T19:49:32Z | FG02 |
| `Nightmare_Eclipse/LegacyHive` | Insufficient description | 2026-07-14T17:43:51Z | FG02 |
| `Nightmare_Eclipse/GreatXML` | Disk-protection claim | 2026-06-11T01:16:19Z | FG02 |
| `Nightmare_Eclipse/GreenPlasma` | Privilege-escalation claim | 2026-06-10T01:23:49Z | FG02 |
| `Nightmare_Eclipse/UnDefend` | Endpoint-disruption claim | 2026-06-10T01:23:25Z | FG02 |
| `Nightmare_Eclipse/BlueHammer` | Vulnerability claim; insufficient detail | 2026-06-10T01:22:52Z | FG02 |
| `Nightmare_Eclipse/YellowKey` | Disk-protection claim | 2026-06-10T01:22:30Z | FG02 |
| `Nightmare_Eclipse/MiniPlasma` | Vulnerability claim | 2026-06-10T01:22:06Z | FG02 |
| `Nightmare_Eclipse/RedSun` | Vulnerability claim; insufficient detail | 2026-06-10T01:20:52Z | FG02 |
| `Nightmare_Eclipse/RoguePlanet` | Endpoint-security claim | 2026-06-09T23:22:01Z | FG02 |

## What this source establishes

The forge exposes repositories under these public namespace labels. It does not independently establish a real identity, community membership, authorship of every commit or a person’s involvement in an intrusion. A similarly spelled namespace is not a verified identity match to the existing research-persona card. Descriptions containing vulnerability or zero-day claims remain publisher statements until corroborated by an appropriate vendor or independent technical source.

No project from this forge was installed, cloned or executed in this release. Licenses, complete commit history and code behavior were not inspected. The source URLs above lead to metadata listings; this catalog is a research reference, not an integration or an operational tool collection.

## Turn the reading into defender questions

| Reading theme | IT/blue-team question | Classroom counterpart |
|---|---|---|
| Endpoint-security claims | Can the owner demonstrate effective protection and independently verified update state? | [RT004](../assessment/modules/RT004.md), [RT006](../assessment/modules/RT006.md) |
| Authentication or credential claims | Which logs and policy controls distinguish ordinary failures from an incident? | [Synthetic triage lab](../foundations/LABS.md#lab-4--triage-synthetic-sign-in-evidence) |
| Privilege configuration | Is broad authority required for the legitimate task? | [RT010](../assessment/modules/RT010.md) |
| Communications/emulation projects | Which engineering claims are documented, measured and applicable? | [Tool interpretation](../foundations/TOOLS.md) |
| Sparse descriptions | What observation is missing before any capability claim is justified? | [RT022](../assessment/modules/RT022.md), [RT023](../assessment/modules/RT023.md) |

These questions are author-designed research prompts, not findings about the repositories or their maintainers. To expand coverage, record the exact public listing page, review date, namespace, description basis and displayed update; keep code-execution analysis separate from metadata review.
