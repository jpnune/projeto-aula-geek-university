#!/usr/bin/env bash
set -o errexit

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Aplicando migrações..."
python manage.py makemigrations --no-input
python manage.py migrate --no-input


echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input --clear
