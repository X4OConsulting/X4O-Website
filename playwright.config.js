// =============================================================================
// Playwright Configuration for X4O Website Test Suite
// =============================================================================
// Configuration file for running automated tests
// Test Script References:
//   - tests/form-functionality.spec.js (Playwright tests)
//   - Tests map to X4O_Test_Cases.csv Test Case IDs
// =============================================================================

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // Test directory
  testDir: './tests',

  // Test file pattern
  testMatch: '**/*.spec.js',

  // Maximum time a test can run (60 seconds)
  timeout: 60000,

  // Maximum time for expect() assertions (10 seconds)
  expect: {
    timeout: 10000,
  },

  // Run tests sequentially in CI, parallel locally
  fullyParallel: false,

  // Fail the build on CI if you accidentally left test.only in the source code
  forbidOnly: !!process.env.CI,

  // Retry failed tests once
  retries: 1,

  // Number of parallel workers
  workers: 1,

  // Reporter configuration
  reporter: [
    ['html', { open: 'never' }],
    ['list'],
  ],

  // Shared settings for all projects
  use: {
    // Base URL for navigation
    baseURL: 'https://x4o.co.za',

    // Collect trace when retrying the failed test
    trace: 'on-first-retry',

    // Screenshot on failure
    screenshot: 'only-on-failure',

    // Navigation timeout
    navigationTimeout: 30000,

    // Action timeout
    actionTimeout: 15000,
  },

  // Browser configurations
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
      },
    },
    {
      name: 'firefox',
      use: {
        ...devices['Desktop Firefox'],
      },
    },
    {
      name: 'webkit',
      use: {
        ...devices['Desktop Safari'],
      },
    },
    // Mobile viewport testing
    {
      name: 'mobile-chrome',
      use: {
        ...devices['Pixel 5'],
      },
    },
    {
      name: 'mobile-safari',
      use: {
        ...devices['iPhone 12'],
      },
    },
  ],
});
