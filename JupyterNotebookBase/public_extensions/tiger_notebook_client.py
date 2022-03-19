# -*- coding:utf-8 -*-
from nbclient.client import NotebookClient
import typing as t
from nbformat.v4.nbbase import output_from_msg
import sys


def output_print_log(out):
    if "text" in out:
        # 写入文件
        print()
        print(out["text"], file=sys.stdout, flush=True)


class TigerNotebookClient(NotebookClient):

    def __init__(self, kc, km):
        super(TigerNotebookClient, self).__init__(self.nb, km)
        self.clear_before_next_output = False
        self.kc = kc

    def output(
        self, outs: t.List, msg: t.Dict, display_id: str, cell_index: int
    ) -> t.Optional[t.List]:

        msg_type = msg['msg_type']

        parent_msg_id = msg['parent_header'].get('msg_id')
        if self.output_hook_stack[parent_msg_id]:
            # if we have a hook registered, it will overrride our
            # default output behaviour (e.g. OutputWidget)
            hook = self.output_hook_stack[parent_msg_id][-1]
            hook.output(outs, msg, display_id, cell_index)
            return None

        try:
            out = output_from_msg(msg)
        except ValueError:
            self.log.error("unhandled iopub msg: " + msg_type)
            return None

        if self.clear_before_next_output:
            self.log.debug('Executing delayed clear_output')
            outs[:] = []
            self.clear_display_id_mapping(cell_index)

        if display_id:
            # record output index in:
            #   _display_id_map[display_id][cell_idx]
            cell_map = self._display_id_map.setdefault(display_id, {})
            output_idx_list = cell_map.setdefault(cell_index, [])
            output_idx_list.append(len(outs))

        outs.append(out)
        output_print_log(out)
        return out