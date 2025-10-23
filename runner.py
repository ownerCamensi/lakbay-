#!/usr/bin/env python3
"""
Lakbay Language Runner - Auto Compile & Execute
Transpiles, compiles, and runs .lakbay files automatically
Supports both g++ and clang++ compilers
"""

from lakbay import compile_lakbay
import sys
import os
import subprocess
import platform

def find_compiler():
    """Find available C++ compiler (g++ or clang++)"""
    compilers = ['clang++', 'g++']
    
    for compiler in compilers:
        try:
            result = subprocess.run([compiler, '--version'], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=5)
            if result.returncode == 0:
                return compiler
        except:
            continue
    
    return None

def main():
    print("╔═══════════════════════════════════════╗")
    print("║   LAKBAY PROGRAMMING LANGUAGE v1.0    ║")
    print("║   Auto-Compile • Auto-Run • Fast 🚀   ║")
    print("╚═══════════════════════════════════════╝")
    print()
    
    # Check if file argument provided
    if len(sys.argv) < 2:
        lakbay_file = 'test.lakbay'
        print(f"📁 No file specified. Using default: {lakbay_file}")
    else:
        lakbay_file = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(lakbay_file):
        print(f"❌ Error: File '{lakbay_file}' not found!")
        print(f"\nUsage: python runner.py <filename.lakbay>")
        sys.exit(1)
    
    print(f"📄 Reading: {lakbay_file}")
    
    # Read source code
    try:
        with open(lakbay_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)
    
    print(f"✓ File loaded ({len(source_code)} characters)")
    print()
    
    # Display source code (optional - comment out if too long)
    print("=" * 50)
    print("LAKBAY SOURCE CODE:")
    print("=" * 50)
    lines = source_code.split('\n')
    if len(lines) > 30:
        for i, line in enumerate(lines[:15], 1):
            print(f"{i:3}: {line}")
        print(f"     ... ({len(lines) - 30} more lines) ...")
        for i, line in enumerate(lines[-15:], len(lines) - 14):
            print(f"{i:3}: {line}")
    else:
        for i, line in enumerate(lines, 1):
            print(f"{i:3}: {line}")
    print("=" * 50)
    print()
    
    # Step 1: Transpile to C++
    print("🔄 [1/3] Transpiling to C++...")
    cpp_code = compile_lakbay(source_code)
    
    if cpp_code.startswith("ERROR:"):
        print(f"❌ Transpilation failed!")
        print(cpp_code)
        sys.exit(1)
    
    print("   ✓ Transpilation successful!")
    
    # Save to file
    output_cpp = 'output.cpp'
    try:
        with open(output_cpp, 'w', encoding='utf-8') as f:
            f.write(cpp_code)
        print(f"   ✓ Saved to: {output_cpp}")
    except Exception as e:
        print(f"   ❌ Error saving file: {e}")
        sys.exit(1)
    
    print()
    
    # Step 2: Find and use compiler
    print("🔨 [2/3] Compiling with C++ compiler...")
    
    compiler = find_compiler()
    
    if not compiler:
        print(f"   ❌ No C++ compiler found!")
        print(f"   Please install g++ or clang++ to compile C++ code.")
        print(f"\n   Installation:")
        if platform.system() == "Linux":
            print(f"     pkg install clang          (Termux)")
            print(f"     sudo apt-get install g++   (Linux)")
        elif platform.system() == "Darwin":
            print(f"     xcode-select --install")
        elif platform.system() == "Windows":
            print(f"     Install MinGW or Visual Studio")
        print(f"\n   Your C++ code is saved in: {output_cpp}")
        print(f"   You can compile it manually with:")
        print(f"     g++ {output_cpp} -o program")
        print(f"     OR")
        print(f"     clang++ {output_cpp} -o program")
        sys.exit(1)
    
    print(f"   ✓ Using compiler: {compiler}")
    
    # Compile
    output_exe = 'program.exe' if platform.system() == 'Windows' else './program'
    compile_cmd = [compiler, output_cpp, '-o', 'program', '-std=c++11']
    
    try:
        result = subprocess.run(compile_cmd, 
                              capture_output=True, 
                              text=True, 
                              timeout=30)
        
        if result.returncode != 0:
            print(f"   ❌ Compilation failed!")
            print(f"\n   Compiler errors:")
            print(result.stderr)
            sys.exit(1)
        
        # Set execute permission (for Linux/Android/macOS)
        if platform.system() != 'Windows':
            try:
                os.chmod('program', 0o755)
            except Exception as e:
                print(f"   ⚠️  Warning: Could not set execute permission: {e}")
        
        print(f"   ✓ Compilation successful!")
        print(f"   ✓ Executable: {output_exe}")
    except subprocess.TimeoutExpired:
        print(f"   ❌ Compilation timed out!")
        sys.exit(1)
    except Exception as e:
        print(f"   ❌ Compilation error: {e}")
        sys.exit(1)
    
    print()
    
    # Step 3: Run the program
    print("▶️  [3/3] Running program...")
    print("=" * 50)
    print("OUTPUT:")
    print("=" * 50)
    
    try:
        # Check if executable exists
        if not os.path.exists('program'):
            print("❌ Executable not found!")
            sys.exit(1)
        
        # Set permissions
        try:
            os.chmod('program', 0o755)
        except Exception as e:
            print(f"⚠️  Permission warning: {e}")
        
        # For Android/Termux - use absolute path
        prog_path = os.path.abspath('program')
        
        # Try execution
        result = subprocess.run([prog_path], 
                              capture_output=True, 
                              text=True, 
                              timeout=10,
                              cwd=os.getcwd())
        
        # Display output
        if result.stdout:
            print(result.stdout)
        else:
            print("(No output)")
        
        if result.stderr:
            print("\nSTDERR:")
            print(result.stderr)
        
        print("=" * 50)
        print(f"Program exited with code: {result.returncode}")
        
    except subprocess.TimeoutExpired:
        print("❌ Program timed out (ran longer than 10 seconds)")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Runtime error: {e}")
        sys.exit(1)
    
    print()
    print("✅ Done!")
    
    # Cleanup option
    print("\n🗑️  Temporary files created:")
    print(f"   - {output_cpp}")
    print(f"   - program (executable)")
    cleanup = input("\nDelete temporary files? (y/n): ").lower().strip()
    if cleanup == 'y':
        try:
            files_deleted = []
            if os.path.exists(output_cpp):
                os.remove(output_cpp)
                files_deleted.append(output_cpp)
            if os.path.exists('program'):
                os.remove('program')
                files_deleted.append('program')
            if os.path.exists('program.exe'):
                os.remove('program.exe')
                files_deleted.append('program.exe')
            
            if files_deleted:
                print(f"   ✓ Deleted: {', '.join(files_deleted)}")
            else:
                print("   ℹ️  No files to delete")
        except Exception as e:
            print(f"   ⚠️  Could not delete some files: {e}")
    else:
        print("   ℹ️  Files kept for inspection")

if __name__ == '__main__':
    main()