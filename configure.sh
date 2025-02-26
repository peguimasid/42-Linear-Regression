python3 -m venv venv
source venv/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual env created!"
    echo "Installing packages:"
    pip install -r requirements.txt
else
    echo "Virtual env is not working!"
fi
