echo "=== Скрипт Фамилия2.sh ==="

cat > testfile.sh << EOF
#!/bin/bash
echo "Это тестовый скрипт, созданный автоматически"
ls -la
EOF

chmod +x testfile.sh

echo "Список всех файлов в длинном формате:"
ls -la

echo " Скрипт выполнен"./