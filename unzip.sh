for f in ./deploy/*.sh; do
  bash "$f" || break
done
