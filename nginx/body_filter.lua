local chunk, eof = ngx.arg[1], ngx.arg[2]
local uri = ngx.var.url
local buffered = ngx.ctx.buffered
local headers = ngx.header
if not buffered then
    buffered = {}
    ngx.ctx.buffered = buffered
end
if chunk ~= "" then
    buffered[#buffered + 1] = chunk
    ngx.arg[1] = nil
end

if ngx.var.namespace ~= nil then
    ngx.log(ngx.ERR, "ngx.var.namespace: "..ngx.var.namespace)
end
if eof then
    local whole = table.concat(buffered)
    ngx.ctx.buffered = nil
    if headers["Content-Type"] ~= nil and string.find(headers["Content-Type"], "text/html") ~= nil then
        local app_id = "proxy/"..ngx.var.namespace
        replaced_data_base_url = string.format('data-base-url="/%s/"', app_id)
        app_id_path = "/"..app_id
        whole = string.gsub(whole, "href=\"/static/", "href=\""..app_id_path.."/static/")
        whole = string.gsub(whole, "src=\"/static/", "src=\""..app_id_path.."/static/")
        whole = string.gsub(whole, "href='/static/", "href='"..app_id_path.."/static/")
        whole = string.gsub(whole, "src='/static/", "src='"..app_id_path.."/static/")
        whole = string.gsub(whole, "href=\"/custom/", "href=\""..app_id_path.."/custom/")
        whole = string.gsub(whole, "src=\"/custom/", "src=\""..app_id_path.."/custom/")
        whole = string.gsub(whole, "'/static/'", "'"..app_id_path.."/static/'")

        whole = string.gsub(whole, "'/custom'", "'"..app_id_path.."/custom'")
        whole = string.gsub(whole, "'/nbextensions'", "'"..app_id_path.."/nbextensions'")
        whole = string.gsub(whole, "'/kernelspecs'", "'"..app_id_path.."/kernelspecs'")
        whole = string.gsub(whole, "\"/kernelspecs", "\""..app_id_path.."/kernelspecs")
        whole = string.gsub(whole, 'data%-base%-url="/"', replaced_data_base_url)
    end
    ngx.arg[1] = whole
end

