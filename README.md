# Build your own Docker

Minimal container runner: execute a command with stdout/stderr relayed and exit with the child process exit code.

## Run

```bash
./run.sh _ _ <command> [args...]
```

Example:

```bash
./run.sh _ _ echo hello
./run.sh _ _ /bin/sh -c "echo world"
```

## Requirements

- Python 3.9+
