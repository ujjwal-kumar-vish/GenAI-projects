# Article Generator

This is part of the GenAI-projects repository, focusing on the article generation features. This project provides a web interface for generating blog articles using AI.

## Project Structure
- `main.py` - Flask application with article generation logic
- `templates/` - HTML templates
  - `index.html` - Main page template
  - `blog.html` - Blog article display template

## Quick start (Linux)

1. Create and activate a virtual environment:

```bash
cd Article_gen
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install flask # Add other dependencies as needed
```

3. Run the application:
```bash
python main.py
```

The application will start on http://127.0.0.1:5000 by default.

## Features
- Web interface for article generation
- Template-based article display
- Flask-based backend

## Contributing
- Create a feature branch off main
- Make your changes
- Open a Pull Request with a clear description
- Include test steps or automated tests

## Next Steps
- Add requirements.txt for dependencies
- Include unit tests
- Add API documentation
- Implement article saving/persistence

## License
This project is part of the GenAI-projects repository. See the repository root for license information.