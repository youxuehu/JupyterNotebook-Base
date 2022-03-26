# -*- coding:utf-8 -*-
from notebook.services.kernels.handlers import ZMQChannelsHandler
from tornado.iostream import StreamClosedError
from tornado.websocket import WebSocketClosedError


class TigerZmqChannelsHandler(ZMQChannelsHandler):

    def _on_zmq_reply(self, stream, msg_list):
        self.log.info("进入自定义 kernel zmq channels tiger")
        # Sometimes this gets triggered when the on_close method is scheduled in the
        # eventloop but hasn't been called.
        if self.ws_connection is None or stream.closed():
            self.log.warning("zmq message arrived on closed channel")
            self.close()
            return
        channel = getattr(stream, "channel", None)
        try:
            msg = self._reserialize_reply(msg_list, channel=channel)
        except Exception:
            self.log.critical("Malformed message: %r" % msg_list, exc_info=True)
            return

        # 处理 msg
        self.log.warn("开始处理 channel message")
        self.log.warn("zmq msg ==> " + msg)

        try:
            self.write_message(msg, binary=isinstance(msg, bytes))
        except (StreamClosedError, WebSocketClosedError):
            self.log.warning("zmq message arrived on closed channel")
            self.close()
            return


_kernel_id_regex = r"(?P<kernel_id>\w+-\w+-\w+-\w+-\w+)"

default_handlers = [
    (r"/api/kernels/%s/channels" % _kernel_id_regex, TigerZmqChannelsHandler),
]
