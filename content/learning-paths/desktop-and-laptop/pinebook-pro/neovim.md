---
title: Installing and Configuring Neovim

weight: 4
layout: learningpathall
---

## Background

This section is optional, and is highly dependant on workflow and preference. This is just one possible setup, and can be replaced with any other code editor on the Pinebook Pro. I am going with Neovim because it is very lightweight and keeps the best parts of Vim while improving on it in many ways. It has Lua extensibility built-in while still supporting Vimscript and so is able to be modified beyond what was possible with Vim, but the vast majority of Vim plugins will still work. 

### Example configurations

When opening it for the first time it will look almost exactly like Vim, but here are some examples showing what can be done with it. These are far more elaborate than the one I will walk you through, but it's nice to see what is possible:
* https://github.com/NvChad/NvChad
* https://github.com/jdhao/nvim-config
* https://github.com/CosmicNvim/CosmicNvim
* https://github.com/ecosse3/nvim
* https://neovim.io/screenshots/

## Installation and setup of Neovim

For this particular setup we will install Python and Node, mainly because they are required for some of the plugins to work correctly without throwing errors each time Neovim is opened.

Also note that Neovim is launched with the nvim command.

### Installation

* Install Neovim
```cmd
sudo pacman -Sy neovim
```

* Install the vim-plug plugin manager
```cmd
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

* Install the Node Version Manager
```cmd
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
```

* Use the Node Version Manager to install the latest long term support version of Node. If the following command doesn't work you may need to restart your terminal emulator
```cmd
nvm install --lts
```

* Install the current release of Python and Pip
```cmd
sudo pacman -Sy python python-pip
```

* Install the Vim Pip dependencies
```cmd
pip3 install pynvim
```

### Configuration / customization

* Create a Neovim init.vim file at ~/.config/nvim/init.vim. The directory most likely won't exist and will need to be created.

* Navigate there and open the file using Neovim
```cmd
nvim init.vim
```

* Copy the following and paste it into the file. Feel free to tweak any settings to your preferences. These were adapted from https://medium.com/geekculture/neovim-configuration-for-beginners-b2116dbbde84 
```
set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching 
set ignorecase              " case insensitive 
set mouse=v                 " middle-click paste with 
set hlsearch                " highlight search 
set incsearch               " incremental search
set tabstop=4               " number of columns occupied by a tab 
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=80                  " set an 80 column border for good coding style
filetype plugin indent on   "allow auto-indenting depending on file type
syntax on                   " syntax highlighting
set mouse=a                 " enable mouse click
set clipboard=unnamedplus   " using system clipboard
filetype plugin on
set cursorline              " highlight current cursorline
set ttyfast                 " Speed up scrolling in Vim

call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')
 Plug 'dracula/vim'
 Plug 'ryanoasis/vim-devicons'
 Plug 'SirVer/ultisnips'
 Plug 'honza/vim-snippets'
 Plug 'scrooloose/nerdtree'
 Plug 'preservim/nerdcommenter'
 Plug 'mhinz/vim-startify'
 Plug 'neoclide/coc.nvim', {'branch': 'release'}
 Plug 'nvim-tree/nvim-web-devicons' " optional, for file icons
 Plug 'nvim-tree/nvim-tree.lua'
call plug#end()

" color schemes
if (has("termguicolors"))
 set termguicolors
endif
syntax enable
" colorscheme evening
colorscheme dracula
" open new split panes to right and below
set splitright
set splitbelow

" move line or visually selected block - alt+j/k
inoremap <A-j> <Esc>:m .+1<CR>==gi
inoremap <A-k> <Esc>:m .-2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv" move split panes to left/bottom/top/right
nnoremap <A-h> <C-W>H
nnoremap <A-j> <C-W>J
nnoremap <A-k> <C-W>K
nnoremap <A-l> <C-W>L" move between panes to left/bottom/top/right
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Press i to enter insert mode, and ii to exit insert mode.
:inoremap ii <Esc>
:inoremap jk <Esc>
:inoremap kj <Esc>
:vnoremap jk <Esc>
:vnoremap kj <Esc>

" open file in a text by placing text and gf
nnoremap gf :vert winc f<cr>" copies filepath to clipboard by pressing yf
:nnoremap <silent> yf :let @+=expand('%:p')<CR>
" copies pwd to clipboard: command yd
:nnoremap <silent> yd :let @+=expand('%:p:h')<CR>" Vim jump to the last position when reopening a file
if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif

lua <<EOF
-- disable netrw at the very start of your init.lua (strongly advised)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- set termguicolors to enable highlight groups
vim.opt.termguicolors = true

-- OR setup with some options
require("nvim-tree").setup({
  sort_by = "case_sensitive",
  view = {
    adaptive_size = true,
    mappings = {
      list = {
        { key = "u", action = "dir_up" },
      },
    },
  },
  renderer = {
    group_empty = true,
  },
  filters = {
    dotfiles = true,
  },
})
EOF
```

* Run the following command inside Neovim to install the plugins listed between the call plug#begin and call plug#end
```cmd
:PlugInstall
```

* One of the plugins, nvim-tree, can be viewed by using the Neovim command. More commands and settings can be seen here: https://github.com/nvim-tree/nvim-tree.lua/blob/master/doc/nvim-tree-lua.txt. Also not covered in this tutorial as it is very much a personal preference, but for the symbols in the tree view to display correctly you will need to download and install a patched font. A good place to choose one is from here: https://github.com/ryanoasis/nerd-fonts
```cmd
:NvimTreeOpen
```
and
```cmd
:NVimTreeClose
```
