[general]

disable segtrap = yes ; same effect with --gst-disable-segtrap

; set default videosink element according to video surface type(X, EVAS, NULL)
videosink element overlay = xvimagesink
videosink element evas = evasimagesink
videosink element fake = fakesink

video converter element =

audiosink element = pulsesink


drmsrc element = filesrc

; if yes. gstreamer will not update registry
skip rescan = yes
delay before repeat = 50 ; msec

; comma separated list of tocken which elemnts has it in it's name will not be used
element exclude keyword = v4l2

; ignore resume play just for debugging
ignore first skip request = no

;audio/video decode type(0:DEFAULT, 1:HW, 2:SW, 3:DISABLE)
video decoder type = 0
audio decoder type = 0

async start = yes

multiple codec supported = yes

; parameters for initializing gstreamer
; DEFAULT SET (--gst-debug=*:2)
gstparam1 = --gst-debug=*:2
gstparam2 =
gstparam3 =
gstparam4 =
gstparam5 =

; generating dot file representing pipeline state
; DEFAULT MUST BE 'no'. If 'yes', mmplayer will set env-variable for it's session as "export GST_DEBUG_DUMP_DOT_DIR=/tmp/"
generate dot = no

; parameter is for only video to be determined
; which clock will be used
; if yes, system clock will be used
; apart from this, audiosink is clock provider for audio
use system clock = yes

; allowed timeout for changing pipeline state
live state change timeout = 30 ; sec
localplayback state change timeout = 10 ; sec

; delay in msec for sending EOS
eos delay = 0 ; msec

; for asm function enable = yes, disable = no
enable asm = yes

[http streaming]

httpsrc element = souphttpsrc

; if set, use file or not use memory for buffering
http file buffer path = /home/owner/content

http buffering limit = 99.0 ; percent

http max size bytes = 1048576 ; bytes

http buffering time = 1.2

http timeout = 30 ; sec
