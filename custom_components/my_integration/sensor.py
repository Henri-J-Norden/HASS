"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([MyIntegrationSensor()])

class MyIntegrationSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "My Integration Sensor"
    _attr_unique_id = "my_integration_sensor"
    _attr_native_unit_of_measurement = None
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self) -> None:
        """Initialize the sensor."""
        super().__init__()

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        return "Hello from My Integration!"
