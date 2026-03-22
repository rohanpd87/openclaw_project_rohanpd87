
<html>
<body>

<h1>OpenClaw Projects</h1>

<h2>Introduction</h2>
<p>
OpenClaw is an AI agent that can perform tasks like running commands,
reading files, and automating work.
</p>

<h2>Requirements</h2>
<ul>
    <li>Node.js</li>
    <li>Python</li>
    <li>Git</li>
    <li>Docker</li>
</ul>

<h2>Verify Installation</h2>
<pre>
node -v
python3 --version
git --version
docker --version
</pre>

<h2>Setup Script (using nano)</h2>
<p>
I created a shell script to automatically check and install required tools.
</p>

<pre>
nano installscript1.sh
</pre>

<p>Paste the following code:</p>

<pre>
#!/bin/bash

echo ""
echo "Starting Development Tools Check..."

# Check Homebrew
echo ""
echo "Checking Homebrew..."
if brew --version >/dev/null 2>&1; then
    echo "Homebrew installed: $(brew --version)"
else
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check Git
echo ""
echo "Checking Git..."
if git --version >/dev/null 2>&1; then
    echo "Git installed: $(git --version)"
else
    echo "Installing Git..."
    brew install git
fi

# Check Python
echo ""
echo "Checking Python..."
if python3 --version >/dev/null 2>&1; then
    echo "Python installed: $(python3 --version)"
    echo "pip version: $(pip3 --version)"
else
    echo "Python not found. Please install from python.org"
fi

# Check Node
echo ""
echo "Checking Node.js..."
if node --version >/dev/null 2>&1; then
    echo "Node installed: $(node --version)"
else
    echo "Installing Node using nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
    \. "$HOME/.nvm/nvm.sh"
    nvm install 22
fi

# Check Docker
echo ""
echo "Checking Docker..."
if docker --version >/dev/null 2>&1; then
    echo "Docker installed: $(docker --version)"
else
    echo "Docker not found. Please install Docker Desktop manually."
fi

echo ""
echo "All checks completed successfully!"
</pre>

<p>Run the script:</p>

<pre>
chmod +x installscript1.sh
./setup.sh
</pre>


<h2>Version Check Screenshot</h2>
<p>
To confirm whether the requirements are installed!
</p>
<img src="/installation docs/Version Check.png" alt="Version Check Screenshot" width="500">

<h2>Projects</h2>

<h3>1. File Organizer</h3>
<p>
Organizes files into folders based on type (images, documents, etc).
</p>

<h2>Tools Used</h2>
<ul>
    <li>Python</li>
    <li>Node.js</li>
</ul>

<h2>Author</h2>
<p>Rohan Prasad</p>

</body>
</html>