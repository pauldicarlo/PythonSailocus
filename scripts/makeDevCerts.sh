#!/bin/bash
# @author: Paul DiCarlo
# @copyright: 2025 Paul DiCarlo
# @license: MIT
# @contact: https://github.com/pauldicarlo

echo "Creating dev certs for project"
echo "Do not check these in, note excluded in .gitignore"

# ===  MAKE SURE IN PROJ ROOT DIR =============================
if [ "$(basename "$PWD")" = "scripts" ]; then
	cd ..
fi

# ===  MAKE CERTS DIR  ========================================
mkdir -p certs
cd certs
rm -rf *

# ===  MAKE TRUSTED ROOT  =====================================
# Create CA root & sign both server/client certs
openssl genrsa -out ca.key 2048
openssl req -x509 \
	-new \
	-nodes \
	-key ca.key \
	-sha256 \
	-days 3650 \
	-out ca.crt \
	-subj "/CN=Dev mTLS CA"

openssl x509 -in ca.crt -noout -dates

# ===  MAKE SERVER CERTS  =====================================
# Create Server Certificate (Signed by CA)
# server private key
openssl genrsa -out server.key 2048
# Create Certificate Signing Request (CSR)
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
# Sign CSR w/CA to create server certificate (add SAN for localhost)
echo "subjectAltName = DNS:localhost,IP:127.0.0.1" > server.ext
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile server.ext

# ===  MAKE CLIENT CERTS  =====================================
# Generate client private key
openssl genrsa -out client.key 2048
# Create CSR
openssl req -new -key client.key -out client.csr -subj "/CN=dev-client"
# Sign with CA (no SAN needed for client certs in most cases)
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365 -sha256


# =====  CREATE PKCS#12 FILE FOR CLIENT CERT  =================
# include CA for chain
PASSWORD=changeit
openssl pkcs12 -export -out client.p12 \
  -inkey client.key \
  -in client.crt \
  -certfile ca.crt \
  -legacy \
  -password pass:$PASSWORD  # TODO: for non-dev situation, use a real password
  echo "FOR Mac..."
  #security import client.p12 -P yourpassword -k ~/Library/Keychains/login.keychain-db
  security import client.p12 -P $PASSWORD -k ~/Library/Keychains/login.keychain-db



# =============================================================
# Cleanup unnecessary files
rm *.csr *.ext *.srl

echo -e "\rDone!\r"