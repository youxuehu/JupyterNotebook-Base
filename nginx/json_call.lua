JSON = (loadfile "JSON.lua")() -- one-time load of the routines

local table = {
    test = "jack"
}
local json_test = JSON:encode(table) -- decode example
local pretty_json_text = JSON:encode_pretty(table) -- "pretty printed" version

local tt1 = JSON:decode(json_test)        -- encode example
local tt2 = JSON:decode(pretty_json_text)        -- encode example

ngx.say(pretty_json_text)