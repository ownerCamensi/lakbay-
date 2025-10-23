#!/bin/bash

# Lakbay Programming Language Installer
# Version 1.0.0

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "╔═══════════════════════════════════════╗"
echo "║   LAKBAY PROGRAMMING LANGUAGE v1.0    ║"
echo "║           Installation Script          ║"
echo "╚═══════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Detect OS
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -d "/data/data/com.termux" ]; then
        OS="termux"
    else
        OS="linux"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
else
    OS="unknown"
fi

echo -e "${BLUE}[INFO]${NC} Detected OS: $OS"
echo ""

# Check Python
echo -e "${YELLOW}[1/5]${NC} Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} Python found: $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} Python 3 not found!"
    echo "Please install Python 3.6 or higher"
    exit 1
fi
echo ""

# Check C++ Compiler
echo -e "${YELLOW}[2/5]${NC} Checking C++ compiler..."
COMPILER=""
if command -v clang++ &> /dev/null; then
    COMPILER="clang++"
    COMPILER_VERSION=$(clang++ --version | head -n 1)
    echo -e "${GREEN}✓${NC} Compiler found: $COMPILER_VERSION"
elif command -v g++ &> /dev/null; then
    COMPILER="g++"
    COMPILER_VERSION=$(g++ --version | head -n 1)
    echo -e "${GREEN}✓${NC} Compiler found: $COMPILER_VERSION"
else
    echo -e "${RED}✗${NC} No C++ compiler found!"
    echo ""
    echo "Installing C++ compiler..."
    
    if [ "$OS" == "termux" ]; then
        pkg install clang -y
    elif [ "$OS" == "linux" ]; then
        sudo apt-get update
        sudo apt-get install g++ -y
    elif [ "$OS" == "macos" ]; then
        echo "Please install Xcode Command Line Tools:"
        echo "  xcode-select --install"
        exit 1
    fi
    
    echo -e "${GREEN}✓${NC} Compiler installed"
fi
echo ""

# Create installation directory
echo -e "${YELLOW}[3/5]${NC} Setting up installation directory..."

if [ "$OS" == "termux" ]; then
    INSTALL_DIR="$HOME/lakbay"
else
    INSTALL_DIR="$HOME/.local/share/lakbay"
fi

mkdir -p "$INSTALL_DIR"
echo -e "${GREEN}✓${NC} Created: $INSTALL_DIR"
echo ""

# Copy files
echo -e "${YELLOW}[4/5]${NC} Installing Lakbay files..."

if [ ! -f "lakbay.py" ] || [ ! -f "runner.py" ]; then
    echo -e "${RED}✗${NC} Installation files not found!"
    echo "Please run this script from the lakbay-lang directory"
    exit 1
fi

cp lakbay.py "$INSTALL_DIR/"
cp runner.py "$INSTALL_DIR/"
echo -e "${GREEN}✓${NC} Files copied to $INSTALL_DIR"

# Copy examples if they exist
if [ -d "examples" ]; then
    cp -r examples "$INSTALL_DIR/"
    echo -e "${GREEN}✓${NC} Examples copied"
fi
echo ""

# Create executable wrapper
echo -e "${YELLOW}[5/5]${NC} Creating lakbay command..."

if [ "$OS" == "termux" ]; then
    BIN_DIR="$HOME/.local/bin"
else
    BIN_DIR="$HOME/.local/bin"
fi

mkdir -p "$BIN_DIR"

# Create lakbay script
cat > "$BIN_DIR/lakbay" << 'EOF'
#!/bin/bash
LAKBAY_DIR="$HOME/.local/share/lakbay"
if [ -d "$HOME/lakbay" ]; then
    LAKBAY_DIR="$HOME/lakbay"
fi
python3 "$LAKBAY_DIR/runner.py" "$@"
EOF

chmod +x "$BIN_DIR/lakbay"
echo -e "${GREEN}✓${NC} Created lakbay command at $BIN_DIR/lakbay"
echo ""

# Add to PATH
SHELL_RC=""
if [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q "$BIN_DIR" "$SHELL_RC"; then
        echo "" >> "$SHELL_RC"
        echo "# Lakbay Programming Language" >> "$SHELL_RC"
        echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$SHELL_RC"
        echo -e "${GREEN}✓${NC} Added to PATH in $SHELL_RC"
        echo -e "${YELLOW}⚠${NC}  Please run: ${BLUE}source $SHELL_RC${NC} or restart your terminal"
    else
        echo -e "${GREEN}✓${NC} PATH already configured"
    fi
fi
echo ""

# Success message
echo -e "${GREEN}"
echo "╔═══════════════════════════════════════╗"
echo "║     Installation Complete! 🎉         ║"
echo "╚═══════════════════════════════════════╝"
echo -e "${NC}"
echo ""
echo "Quick Start:"
echo "  1. Create a file: hello.lakbay"
echo "  2. Run: lakbay hello.lakbay"
echo ""
echo "Or try an example:"
if [ -d "$INSTALL_DIR/examples" ]; then
    echo "  lakbay $INSTALL_DIR/examples/calculator.lakbay"
fi
echo ""
echo "Documentation: https://github.com/yourusername/lakbay-lang"
echo ""
echo -e "${BLUE}Happy coding with Lakbay! 🚀${NC}"
echo ""