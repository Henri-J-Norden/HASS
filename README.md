# Home Assistant Custom Component

This is a custom component for Home Assistant.

## Installation

### HACS Installation (Recommended)
1. Make sure you have [HACS](https://hacs.xyz) installed in your Home Assistant instance
2. Add this repository to HACS:
   - Click on HACS in the sidebar
   - Click on "Integrations"
   - Click the three dots in the top right corner
   - Select "Custom repositories"
   - Add the URL of this repository
   - Select "Integration" as the category
3. Click on "+ Explore & Download repositories" 
4. Search for "My Integration"
5. Click Download
6. Restart Home Assistant

### Manual Installation
1. Copy the `custom_components` directory to your Home Assistant configuration directory
2. Restart Home Assistant

## Configuration

Add the following to your `configuration.yaml`:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: my_integration
```

## Requirements

- Home Assistant version 2024.2.0 or higher

## License

This project is licensed under the MIT License - see the LICENSE file for details
