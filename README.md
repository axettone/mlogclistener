# mlogclistener
A simple remote listener for mlogc (ModSecurity remote audit log tool)

## Setup
Copy config.yml.example to config.yml and set host and port.
Warning: on \*nix systems you must be root to use port < 1025.

Generate a PEM certificate
```shell
openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key.pem -out tmpcert.pem
cat tmpcert.pem key.pem > cert.pem
```