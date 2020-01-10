import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light, output
from esphome.const import CONF_BLUE, CONF_GREEN, CONF_RED, CONF_OUTPUT_ID, \
    CONF_WARM_WHITE, CONF_COLD_WHITE_COLOR_TEMPERATURE, \
    CONF_WARM_WHITE_COLOR_TEMPERATURE

rgbw_ecct_ns = cg.esphome_ns.namespace('rgbw_ecct')
RGBWECCTLightOutput = rgbw_ecct_ns.class_('RGBWECCTLightOutput', light.LightOutput)

CONFIG_SCHEMA = light.RGB_LIGHT_SCHEMA.extend({
    cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(RGBWECCTLightOutput),
    cv.Required(CONF_RED): cv.use_id(output.FloatOutput),
    cv.Required(CONF_GREEN): cv.use_id(output.FloatOutput),
    cv.Required(CONF_BLUE): cv.use_id(output.FloatOutput),
    cv.Required(CONF_WARM_WHITE): cv.use_id(output.FloatOutput),
    cv.Required(CONF_COLD_WHITE_COLOR_TEMPERATURE): cv.color_temperature,
    cv.Required(CONF_WARM_WHITE_COLOR_TEMPERATURE): cv.color_temperature,
})


def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    yield light.register_light(var, config)

    red = yield cg.get_variable(config[CONF_RED])
    cg.add(var.set_red(red))
    green = yield cg.get_variable(config[CONF_GREEN])
    cg.add(var.set_green(green))
    blue = yield cg.get_variable(config[CONF_BLUE])
    cg.add(var.set_blue(blue))
    cg.add(var.set_cold_white_temperature(config[CONF_COLD_WHITE_COLOR_TEMPERATURE]))
    wwhite = yield cg.get_variable(config[CONF_WARM_WHITE])
    cg.add(var.set_warm_white(wwhite))
    cg.add(var.set_warm_white_temperature(config[CONF_WARM_WHITE_COLOR_TEMPERATURE]))
