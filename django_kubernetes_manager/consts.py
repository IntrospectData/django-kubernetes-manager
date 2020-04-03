PULL_POLICY = [
    ('Always', 'Always'),
    ('IfNotPresent', 'IfNotPresent'),
    ('Never', 'Never')
]

RESTART_POLICY = [
    ('Always', 'Always'),
    ('OnFailure', 'OnFailure'),
    ('Never', 'Never')
]

byte_units = {
    "E": 1000**6, "P": 1000**5, "T": 1000**4,
    "G": 1000**3, "M": 1000**2, "K": 1000,
    "Ei": 1024**6, "Pi": 1024**5, "Ti": 1024**4,
    "Gi": 1024**3, "Mi": 1024**2, "Ki": 1024
}
