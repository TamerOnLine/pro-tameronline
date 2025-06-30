# docs/main.py

from mkdocs_macros.plugin import define_env

def define_env(env):
    @env.macro
    def read_file(path):
        with open(path, encoding='utf-8') as f:
            return f.read()
        
print("✅ main.py loaded successfully")

