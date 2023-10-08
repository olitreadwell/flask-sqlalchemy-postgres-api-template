module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react/jsx-runtime",
    "plugin:react-hooks/recommended",
  ],
  ignorePatterns: ["dist", ".eslintrc.cjs"],
  parserOptions: { ecmaVersion: "latest", sourceType: "module" },
  settings: { react: { version: "18.2" } },
  plugins: ["react-refresh"],
  rules: {
    // Stylistic rules
    indent: ["warn", 2, { SwitchCase: 1 }],

    // Enforces consistent linebreak style (unix)
    "linebreak-style": ["warn", "unix"],

    // Enforces the use of single quotes for strings
    quotes: ["warn", "double"],

    // Enforces semicolons at the end of statements
    semi: ["warn", "always"],

    // Limits lines of code and comments to 60 characters per line
    "max-len": ["warn", { code: 80, comments: 80 }],

    // Best practices
    // Warns against the use of console statements
    "no-console": "warn",

    // JavaScript language features

    // Warns about unreachable code
    "no-unreachable": "warn",

    // Warns about unused expressions
    "no-unused-expressions": "warn",

    // Warns about unused labels
    "no-unused-labels": "warn",

    // Warns about unused variables
    "no-unused-vars": "warn",

    // Warns about empty blocks/statements
    "no-empty": "warn",

    // Warns about empty character classes in regular expressions
    "no-empty-character-class": "warn",

    // Warns about empty function declarations
    "no-empty-function": "warn",

    // Warns about empty object patterns
    "no-empty-pattern": "warn",

    // Warns about unnecessary boolean casts
    "no-extra-boolean-cast": "warn",

    // Warns about unnecessary semicolons
    "no-extra-semi": "warn",

    // Warns about unnecessary lone blocks
    "no-lone-blocks": "warn",

    // Warns about unnecessary function callings
    "no-useless-call": "warn",

    // Warns about unnecessary try/catch blocks
    "no-useless-catch": "warn",

    // Warns about unnecessary string concatenation
    "no-useless-concat": "warn",

    // Warns about unnecessary constructor declarations
    "no-useless-constructor": "warn",

    // Warns about unnecessary escape characters
    "no-useless-escape": "warn",

    // Warns about unnecessary return statements
    "no-useless-return": "warn",

    // Warns about code complexity exceeding a maximum threshold
    complexity: ["warn", { max: 15 }],

    // Warns about excessive nested code blocks
    "max-depth": "warn",

    // Warns about files exceeding a maximum number of lines (excluding blank lines and comments)
    "max-lines": [
      "warn",
      { max: 60, skipBlankLines: true, skipComments: true },
    ],

    // Warns about functions exceeding a maximum number of lines (excluding blank lines and comments)
    "max-lines-per-function": [
      "warn",
      { max: 40, skipBlankLines: true, skipComments: true },
    ],

    // Warns about excessive nested callbacks
    "max-nested-callbacks": "warn",

    // Warns about functions exceeding a maximum number of statements
    "max-statements": "warn",
    "react-refresh/only-export-components": [
      "warn",
      { allowConstantExport: true },
    ],
  },
};
