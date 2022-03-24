mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base='light'\n\
primaryColor='purple'\n\
backgroundColor='lightgrey'\n\
secondaryBackgroundColor='#e8eef9'\n\
textColor='black'\n\
\n\"
" > ~/.streamlit/config.toml