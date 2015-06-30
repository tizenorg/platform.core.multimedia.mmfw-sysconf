; < Camera/Camcorder Configure Main INI file >
;
; - SDK Camera
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
;GSTInitOption = --gst-debug=3,avsysvideosrc:4 || NOT-USE-DEFAULT_VALUE
ModelName = TIZEN_SDK
;DisabledAttributes = camera-optical-zoom camera-af-touch-x camera-af-touch-y camera-exposure-value camera-f-number camera-shutter-speed camera-hold-af-after-capturing filter-flip filter-hue display-src-x display-src-y display-src-width display-src-height tag-image-description strobe-control strobe-capabilities strobe-mode detect-mode detect-number detect-focus-select detect-select-number detect-status || NO_DEFAULT_VALUE

[VideoInput]
UseConfCtrl = 1
ConfCtrlFile0 = mmfw_camcorder_dev_video_pri.ini
ConfCtrlFile1 = mmfw_camcorder_dev_video_sec.ini
VideosrcElement = v4l2src | 1,1 | do-timestamp,1 | device,/dev/video0
UseVideoscale = 0
VideoscaleElement = videoscale | 3,0 | width,320 | height,240 | method,1
UseZeroCopyFormat = 0
DeviceCount = 2

[AudioInput]
AudioDevice = 0,1 || 0
AudiosrcElement = pulsesrc | 2,0 | do-timestamp,1 | blocksize,640
AudiomodemsrcElement = pulsesrc | 2,0 | do-timestamp,1 | blocksize,640

[VideoOutput]
; DisplayDevice
;;; 0: MAIN LCD, 1: SUB LCD, 2:TV OUT, 3: MAIN LCD and SUB LCD, 4: MAIN LCD and TV OUT
DisplayDevice = 0 || 0
; Videosink
;;; 0: X surface, 1: Evas surface, 2: GL surface, 3: NULL surface
Videosink = 0,1,3 || 0
VideosinkElementX = xvimagesink | 6,0 | draw-borders,0 | force-aspect-ratio,1 | enable-last-sample,0 | qos,0 | sync,0 | show-preroll-frame,0
VideosinkElementEvas = evasimagesink | 4,0 | enable-last-sample,0 | qos,0 | sync,0 | show-preroll-frame,0
VideosinkElementNull = fakesink | 3,0 | qos,0 | sync,0 | enable-last-sample,0
UseVideoscale = 0
VideoscaleElement = videoscale | 1,0 | method,1

[VideoEncoder]
H263 = emulenc_h263p | 0,0
MPEG4 = emulenc_mpeg4 | 0,0
THEORA = theoraenc | 1,0 | num-bufs,4

[AudioEncoder]
AMR = amrnbenc | 0,0
AAC = ffenc_aac | 0,0
WAVE = wavenc | 0,0
VORBIS = vorbisenc | 0,0

[ImageEncoder]
JPEG = jpegenc | 0,0
PNG = pngenc | 0,0

[Capture]
UseEncodebin = 1
UseCaptureMode = 0
VideoscaleElement = videoscale | 1,0 | method,1
PlayCaptureSound = 0

[Record]
UseAudioEncoderQueue = 1
UseVideoEncoderQueue = 1
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
ImageAutoColorSpace = 0
RecordsinkElement = filesink | 1,0 | async,0
UseNoiseSuppressor = 0
DropVideoFrame = 0
PassFirstVideoFrame = 0

[Mux]
3GP = ffmux_3gp | 0,0
AMR = ffmux_amr | 0,0
MP4 = ffmux_mp4 | 0,0
OGG = oggmux | 0,0
WAV = wavenc | 0,0
AAC = ffmux_adts | 0,0

