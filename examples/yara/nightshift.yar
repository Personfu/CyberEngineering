rule NightshiftTrainingMarker {
    meta:
        purpose = "Harmless classroom marker, not malware identification"
    strings:
        $marker = "NIGHTSHIFT-TRAINING-ONLY" ascii
    condition:
        filesize < 1024 and $marker
}
