JSON = (loadfile "JSON.lua")() -- one-time load of the routines

local table = {
    "name": "jack"
}
local lua_value = JSON:decode(table) -- decode example


local raw_json_text    = JSON:encode(lua_value)        -- encode example
local pretty_json_text = JSON:encode_pretty(lua_value) -- "pretty printed" version