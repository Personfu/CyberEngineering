# Evidence lab: hashes, a harmless rule and a toy binary

**Outcome:** a small inspectable chain from source input to tool output. All example data is fictional or authored in this repository.

## 1. Preserve original bytes

Use a copy of a harmless fixture. Record source path, acquisition time, byte count and SHA-256 before analysis. For artifacts with a publisher digest, compare against that independently obtained value rather than copying the newly calculated hash into the expected field.

```bash
openssl dgst -sha256 labs/fixtures/example.bin
```

OpenSSL is optional; the standard-library verification helper can do the digest comparison. A hash match establishes byte equality to the expected digest, not who authored the bytes or whether an executable is safe.

## 2. Write an explainable YARA rule

The [original classroom rule](../../examples/yara/nightshift.yar) matches a marker deliberately placed in [training.txt](../../examples/yara/training.txt). If the YARA CLI is installed:

```bash
yara examples/yara/nightshift.yar examples/yara/training.txt
yara examples/yara/nightshift.yar labs/fixtures/health.json
```

Expected: the marker rule matches the first file and does not match the second. A rule condition holding is the entire conclusion; it does not identify malware. Try moving the marker beyond the rule’s file-size limit and explain why the outcome changes. See the [official rule syntax](https://yara.readthedocs.io/en/stable/writingrules.html).

## 3. Compile a binary whose source you know

With a C compiler installed:

```bash
cc -O0 -g examples/benign_counter.c -o /tmp/nightshift-counter
/tmp/nightshift-counter
```

Expected output: `observed=3`. Inspect this binary in Ghidra: identify `main`, the loop and the constant limit, then compare disassembly/decompilation with the source. Optimize a second build and explain why the representation changes without changing the expected output. Decompiled text is a reconstruction, not the original C source. No unknown binary is downloaded or run.

## 4. Read offline protocol structures

```bash
python -m labtools.benchkit ble-decode 02010605094c414231
```

The fictional advertisement decodes Flags and the local name `LAB1`. A malformed length must be rejected. A name or manufacturer-data field is an observation, not proof of a device vendor, operator, surveillance function or physical location.

## 5. Hand off a bounded conclusion

Include input digests, source/program version, command, relevant output, interpretation and limits. Label synthetic fixtures. Keep facts separate from inferred identity. Record failed and negative cases. An evidence handoff should let another person repeat the analysis without needing your shell history or unrelated private records.

**References:** [YARA rules](https://yara.readthedocs.io/en/stable/writingrules.html), [OpenSSL digests](https://docs.openssl.org/master/man1/openssl-dgst/), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [forensic evidence research](../../atlas/06-forensic-science.md).
