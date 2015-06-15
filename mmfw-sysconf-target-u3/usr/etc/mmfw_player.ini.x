[general]

; if disabled typefind element will used directely
use decodebin = yes

; for retransmission enable = yes, disable = no
use rtp retransmission = no

disable segtrap = yes ; same effect with --gst-disable-segtrap

; set default videosink element according to video surface type(X, EVAS, NULL)
videosink element x = xvimagesink
videosink element evas = evasimagesink
videosink element fake = fakesink

video converter element =

audiosink element = alsasink


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

; parameter for clock provide in audiosink
provide clock for music = yes
provide clock for movie = yes

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


[rtsp streaming]

rtspsrc element = rtspsrc

rtsp buffering time = 5000; msec

rtsp rebuffering time = 15000; msec

rtsp do typefinding = no; if no, caps on rtspsrc:src pad will be used for autoplugging

rtsp error concealment = yes

;transport to use, 7 for default (tcp+udp-multicast+udp-unicast), 4 for TCP
rtsp lower protocol = 7;

[hw accelation]
use video hw accel = no


[priority]

use priority setting = no

demux = 95

videosink = 96

audiosink = 97

ringbuffer = 98

[subtitle]
; related to the textbin structure
; if yes, textbin need to consider the external display to print subtitle
support external display = no

;  subtitle default value when 'support external display = yes'
mirroring width = 1920

mirroring height = 1080

font color = 0xffffffff

font background color = 0x00000000

