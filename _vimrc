python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline, even if there is only one tab
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)
set t_Co=256

set nowrap
set smartindent
set expandtab
set shiftwidth=2
set number
colorscheme desert
set clipboard=unnamedplus

set wildignore+=*/tmp/*,*.so,*.swp,*.zip

" CTRLP
set runtimepath^=~/.vim/bundle/ctrlp.vim
let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn)|node_modules$'

" NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
map <C-n> :NERDTreeToggle<CR>

