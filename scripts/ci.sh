sudo apt install p7zip-full -y

npm run build

cd Chinese
zip -r -q ../cn.zip .
cd ..

cd "English(US)"
zip -r -q ../en.zip .
cd ..