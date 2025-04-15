# Why, oh why
People send me text memos.
I have to listen to them.
This takes a long time and I have to skip back and forth if I need to "reread", this is haphazard.

I hate voice memos and always want text memos.
Now I can always have voice memos with
```sh
./transcribe.sh $THAT_PESKY_OGG_SOMEONE_SENT_ME
```

The shell script sets up a venv for you and installs stuff if necessary.
Not super robust.
It then invokes the Python script, which does the library legwork.
