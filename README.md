# HashCalcPro

HashCalcPro is a portable Windows hash-calculation utility with a Tkinter interface and command-line support.

## Supported algorithms

- SHA-1
- SHA-256
- SHA-512
- MD5
- CRC-32

## Run from source

```bash
python main.pyw
```

To calculate a hash from the command line:

```bash
python main.pyw SHA-256 path\\to\\file
```

## Downloads

Prebuilt Windows binaries are published under [GitHub Releases](../../releases).

## Build

The `main.spec` file can be used with PyInstaller:

```bash
pyinstaller main.spec
```

The repository also retains the original Visual C++/CLI solution as a historical project artifact; the Python source is the functional hash utility.
