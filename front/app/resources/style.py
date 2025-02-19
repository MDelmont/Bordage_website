#!/usr/bin/env python
# -*- coding: utf-8 -*-


class default_style_page():
  def __init__(self):
    self.style = {      'style_part_of_page': {'width': '100%','padding-top':'10px','padding-down':'10px','textAlign': 'center'},
                        'style_part_of_form': {'width': '100%','padding-top':'5px','padding-down':'5px','textAlign': 'center'},
                        'text_align_center': {'textAlign': 'center'},
                        'padding_top_5': {'padding-top':'5%'},
                        'width_100_text_align_center': {'width': '100%','textAlign': 'center'},
                        'style_form': {'width': '75%', 'display': 'inline-block','textAlign': 'center'},
                        'style_col': None,
                        'style_case': None,
                        
                     }

  def get_default_style(self):
    return self.style['style_part_of_page'], self.style['style_part_of_form'],self.style['style_form'], self.style['style_col'], self.style['style_case']

class style_vue_desemble(default_style_page):
    def __init__(self):
        super().__init__()
        self.style.update( {

                        'style_case_select_simulation':{'width': '100%','textAlign': 'center','vertical-align': 'top', 'display': 'inline-block'}, 
                        
                     })
