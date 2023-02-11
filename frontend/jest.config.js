const nextJest = require('next/jest')

const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})

// Add any custom config to be passed to Jest
const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    // Handle module aliases (this will be automatically configured for you soon)
    '^@/components/(.*)$': '<rootDir>/components/$1',
    // '^@/utils/(.*)$': '<rootDir>/utils/$1',
    '^@/pages/(.*)$': '<rootDir>/pages/$1',
  },
  testEnvironment: 'jest-environment-jsdom',
  collectCoverageFrom: [
    '**/*.{ts,jsx,tsx}',
    '!**/coverage/**',
    '!**/jest.config.js',
    '!**/next.config.js',
    '!**/node_modules/**',
    '!**/vendor/**',
    '!**/__test__/**',
    '!**/hooks/**',
    '!**/utils/**',
  ],

  modulePathIgnorePatterns: [
    "/_test__/menuItemsForTests.ts",
  ],
  rootDir: "./",
  modulePaths: [
    "<rootDir>"
  ],
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
module.exports = createJestConfig(customJestConfig)
