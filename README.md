# EncryptionTool

Encrypt and decrypt files in the browser. Nothing is uploaded; everything runs locally.

Open `index.html` in Chrome, Edge, Firefox or Safari. It works offline.

- **Encrypt:** upload a public key and a file (up to 10 MB). `ABC.zip` downloads as `ABC_Encrypted.zip`.
- **Decrypt:** upload the private key and the encrypted file. It downloads as `ABC_Decrypted.zip`.

## Keys

- **PGP (`.asc`):** output is a standard OpenPGP message that GnuPG can decrypt. Keys with a passphrase are supported on decrypt.
- **RSA PEM:** a random AES-256-GCM key encrypts the file and is wrapped with RSA-OAEP (SHA-256). Only this tool decrypts it.

## Build

`index.html` is generated from `src/index.src.html` with OpenPGP.js inlined.

    npm install
    cd src && python3 build.py
