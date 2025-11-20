# Contributing to E-Voting System

Thank you for your interest in contributing to the E-Voting System! 🗳️

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/e-voting.git
   cd e-voting
   ```
3. **Set up the development environment** following the [SETUP.md](SETUP.md) guide

## Development Process

### Backend Development (Flask/Python)

1. **Create virtual environment:**

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate   # Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the backend:**
   ```bash
   python app.py
   ```

### Frontend Development (React/TypeScript)

1. **Install dependencies:**

   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm start
   ```

## Making Changes

1. **Create a new branch** for your feature:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards below

3. **Test your changes** thoroughly

4. **Commit your changes** with descriptive messages:

   ```bash
   git commit -m "Add: new voting validation feature"
   ```

5. **Push to your fork:**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## Coding Standards

### Python (Backend)

- Follow **PEP 8** style guide
- Use **type hints** where possible
- Add **docstrings** for functions and classes
- Write **unit tests** for new features
- Use **descriptive variable names**

### TypeScript/React (Frontend)

- Use **functional components** with hooks
- Follow **React best practices**
- Use **TypeScript** for type safety
- Add **proper error handling**
- Write **clean, readable code**

### General Guidelines

- **Security first** - never commit sensitive data
- **Test thoroughly** - test on multiple browsers/OS
- **Document changes** - update README if needed
- **Keep commits atomic** - one feature per commit
- **Write clear commit messages**

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review of the code completed
- [ ] Code is properly commented
- [ ] Changes tested locally
- [ ] No merge conflicts
- [ ] Documentation updated if needed

### PR Description Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [ ] Frontend tested
- [ ] Backend tested
- [ ] Integration tested

## Screenshots (if applicable)

Add screenshots of UI changes
```

## Security Guidelines

⚠️ **NEVER commit sensitive information:**

- API keys or secrets
- Database credentials
- Email passwords
- Private keys or certificates
- User data or test accounts

✅ **Always:**

- Use environment variables for secrets
- Validate all user inputs
- Implement proper authentication
- Follow OWASP security guidelines
- Test for SQL injection and XSS

## Reporting Issues

- **Security issues**: Email directly (don't create public issues)
- **Bugs**: Use the bug report template
- **Feature requests**: Use the feature request template
- **Questions**: Create a discussion thread

## Code of Conduct

- Be respectful and inclusive
- Help others learn and grow
- Focus on constructive feedback
- Maintain a professional tone
- Follow GitHub's community guidelines

## Getting Help

- **Documentation**: Check [README.md](README.md) and [SETUP.md](SETUP.md)
- **Issues**: Search existing issues first
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Create an issue for project-related questions

## Recognition

Contributors will be acknowledged in:

- README.md contributors section
- Release notes for significant contributions
- Special recognition for security improvements

Thank you for contributing to making digital voting more accessible and secure! 🎉
