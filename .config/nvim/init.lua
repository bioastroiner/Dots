vim.cmd([[
" https://neovim.io/doc/user/nvim/#nvim-from-vim
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
source ~/.vimrc
if exists(':tnoremap')

  tnoremap <Esc> <C-\><C-n>

endif
]])
require("config.lazy")
