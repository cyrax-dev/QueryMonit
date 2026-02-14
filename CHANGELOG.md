# Changelog

## [2.0.0] - 2026-02-14

### Added
- Added retry system for A2S queries
- Automatic exe build via GitHub Actions
- Handling server unavailability
- Support for custom offline status text via the `offline` field in servers.json

### Changed
- Improved service architecture
- Project structure optimized

### Fixed
- A2S timeouts fixed
- Fixed freeze-build issues

---

## [1.0.0] - 2025-09-23

### Features
- Run multiple Discord bots simultaneously
- Check server status (online/offline)
- Display the number of players, slots, and queue
- Support for status templates: ‘status_template’: ‘🟢 {players}/{slots} | {time} | ➕{queue}’

### Archive contents:
- QueryMonit.exe — ready-to-run executable file for Windows
- servers.json — example server configuration
