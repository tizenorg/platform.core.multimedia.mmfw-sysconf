; < Camera/Camcorder Configure Main INI file >
;
; - Header List -
; 1.  General
; 2.  VideoInput
; 3.  AudioInput
; 4.  VideoOutput
; 5.  Capture
; 6.  Record
; 7.  VideoEncoder
; 8.  AudioEncoder
; 9.  ImageEncoder
; 10. Mux
;
; - Note -
; If you want to add a new header,
; add a new enum value to "enum ConfigureCategoryMain"
; and new default table for it in mm_camcorder_configure.c/.h
;

[General]
SyncStateChange = 1
;GSTInitOption = --gst-enable-tiny-registry --gst-disable-segtrap || NOT-USE-DEFAULT_VALUE
;GSTInitOption = --gst-enable-tiny-registry --gst-disable-segtrap --gst-debug=3 || NOT-USE-DEFAULT_VALUE
ModelName = GT-TIZEN
;DisabledAttributes = camera-optical-zoom camera-af-touch-x camera-af-touch-y camera-exposure-value camera-f-number camera-shutter-speed camera-hold-af-after-capturing filter-flip filter-hue display-src-x display-src-y display-src-width display-src-height tag-image-description strobe-control strobe-capabilities strobe-mode detect-mode detect-number detect-focus-select detect-select-number detect-status || NO_DEFAULT_VALUE

[VideoInput]
UseConfCtrl = 1
ConfCtrlFile0 = mmfw_camcorder_dev_video_pri.ini
ConfCtrlFile1 = mmfw_camcorder_dev_video_sec.ini
VideosrcElement = tvcamerasrc | 1,1 | do-timestamp,1 | device,/dev/video241
UseVideoscale = 1
VideoscaleElement = videoscale | 3,0 | width,320 | height,240 | method,1
UseZeroCopyFormat = 0
DeviceCount = 1

[AudioInput]
AudioDevice = 0 || 0
AudiosrcElement = pulsesrc | 1,0 | do-timestamp,1

[VideoOutput]
; DisplayDevice
;;; 0: MAIN LCD, 1: SUB LCD, 2:TV OUT, 3: MAIN LCD and SUB LCD, 4: MAIN LCD and TV OUT
DisplayDevice = 0 || 0
; DisplayMode
;;; 0: Default, 1: Pri Video ON and Sec Video Full-Screen, 2: Pri Video OFF and Sec Video Full-Screen
DisplayMode = 0,1,2 || 0
; Videosink
;;; 0: Overlay surface, 1: Evas surface, 2: GL surface, 3: NULL surface, 4: Remote
Videosink = 0,3,4 || 3
VideosinkElementOverlay = xvimagesink | 6,0 | draw-borders,0 | force-aspect-ratio,1 | enable-last-sample,0 | qos,0 | sync,0 | show-preroll-frame,0
VideosinkElementRemote = shmsink | 5,0 | wait-for-connection,0 | perms,511 | enable-last-sample,0 | qos,0 | sync,0
VideosinkElementNull = fakesink | 4,0 | qos,0 | sync,0 | enable-last-sample,0 | show-preroll-frame,0
UseVideoscale = 1
VideoscaleElement = fimcconvert | 1,0 | rotang,0

[VideoEncoder]
MPEG4 = avenc_mpeg4 | 0,0

[AudioEncoder]
AMR = amrnbenc | 0,0
AAC = avenc_aac | 1,0 | compliance,-2
WAVE = wavenc | 0,0
MP3 = lame | 0,0

[ImageEncoder]
JPEG = jpegenc | 0,0
;PNG = pngenc | 0,0

[Capture]
UseEncodebin = 0
UseCaptureMode = 0
VideoscaleElement = videoscale | 1,0 | method,1

[Record]
UseAudioEncoderQueue = 1
UseVideoEncoderQueue = 0
VideoProfile = 0
VideoAutoAudioConvert = 1
VideoAutoAudioResample = 0
VideoAutoColorSpace = 0
AudioProfile = 1
AudioAutoAudioConvert = 1
AudioAutoAudioResample = 0
AudioAutoColorSpace = 0
ImageProfile = 2
ImageAutoAudioConvert = 0
ImageAutoAudioResample = 0
ImageAutoColorSpace = 1
RecordsinkElement = filesink | 1,0 | async,0
UseNoiseSuppressor = 0
DropVideoFrame = 0
PassFirstVideoFrame = 0

[Mux]
3GP = avmux_3gp | 0,0
AMR = avmux_amr | 0,0
MP4 = avmux_mp4 | 0,0
AVI = avimux | 0,0
MATROSKA = matroskamux | 0,0
WAV = wavenc | 0,0
AAC = avmux_adts | 0,0
M2TS = mpegtsmux | 0,0
