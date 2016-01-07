[general]

; if disabled typefind element will used directely
use decodebin = no ; async state change problem exist

use sink handler = yes

disable segtrap = yes ; same effect with --gst-disable-segtrap

; set default videosink element according to video surface type(X, EVAS, NULL)
videosink element overlay = xvimagesink
videosink element evas = evasimagesink
videosink element fake = fakesink

video converter element = ffmpegcolorspace

audiosink element = avsysaudiosink

drmsrc element = filesrc

; if yes. gstreamer will not update registry
skip rescan = yes
delay before repeat = 50 ; msec

; comma separated list of tocken which elemnts has it in it's name will not be used
element exclude keyword = ffdec_, omx_, v4l2

async start = yes

multiple codec supported = yes

; parameters for initializing gstreamer
gstparam1 =
gstparam2 =
gstparam3 =
gstparam4 =
gstparam5 =

; generating dot file representing pipeline state
generate dot = no

; parameter for clock provide in audiosink
provide clock = yes

; allowed timeout for changing pipeline state
live state change timeout = 30 ; sec
localplayback state change timeout = 10 ; sec

; delay in msec for sending EOS
eos delay = 150 ; msec


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


[hw accelation]
use video hw accel = no


[priority]

use priority setting = no

demux = 95

videosink = 96

audiosink = 97

ringbuffer = 98
