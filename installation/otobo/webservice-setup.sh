#!/usr/bin/env bash
set -e

# Parameter aus der Umgebung
if [ "${OTOBO_INTEGRATION}" != "true" ]; then
  echo "OTOBO-Integration deaktiviert, kein Setup nötig."
  exit 0
fi

if [ "${OTOBO_DOCKER_INSTALLATION}" = "true" ]; then
  OTOBO_CLI="docker exec -i ${OTOBO_CONTAINER_NAME} bin/otobo.Console.pl"
else
  OTOBO_CLI="${OTOBO_PATH}/bin/otobo.Console.pl"
fi
BASHRC_FILE="${HOME}/.bashrc"

OTOBOPASS=$(openssl rand -base64 48 \
  | tr -dc 'A-Za-z0-9!@#$%^&*()_+[]{}|:;,.<>?-' \
  | head -c 64)

VAR_LINE="export OTOBOPASS=\"${OTOBOPASS//\"/\\\"}\""
COMMENT="# ATC OTOBO-Passwort"

if grep -q "^${COMMENT}" "${BASHRC_FILE}"; then
  sed -i'' -e "/^${COMMENT}/,+1c\\
${COMMENT}
${VAR_LINE}
" "${BASHRC_FILE}"
else
  {
    echo ""
    echo "${COMMENT}"
    echo "${VAR_LINE}"
  } >> "${BASHRC_FILE}"
fi

export OTOBOPASS

$OTOBO_CLI Admin::User::Add \
  --user-name atc_user \
  --first-name ATC \
  --last-name System \
  --password "$OTOBOPASS" \
  --email atc@example.com \
  --comment "Benutzer für ATC-Connector" \

$OTOBO_CLI Admin::WebService::Add \
  --name OTAI \
  --source-path "/var/webservices/otai.yml" \

echo "OTOBO-Setup abgeschlossen."
