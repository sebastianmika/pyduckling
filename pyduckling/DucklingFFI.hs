{-# LANGUAGE ForeignFunctionInterface #-}
module Pyduckling where
 
import Foreign.C.Types
import Foreign.C.String
import Data.String
-- import Control.Monad.IO.Class
import qualified Data.Text as Text
-- import qualified Data.Text.Encoding as Text
import Data.Time
import Data.Time.Clock.POSIX
import Data.Time.LocalTime.TimeZone.Series
import Data.Maybe
import Text.Read (readMaybe)

import Duckling.Core
import Duckling.Types
import Duckling.Resolve

-- | Builds a `DucklingTime` for timezone `tz` at `utcTime`.
-- If no `series` found for `tz`, uses UTC.
_makeReftime :: TimeZoneSeries -> UTCTime -> DucklingTime
_makeReftime tzs utcTime = DucklingTime $ ZoneSeriesTime utcTime tzs

millisToUTC :: Integer -> UTCTime
millisToUTC t = posixSecondsToUTCTime $ (fromInteger t) / 1000

foreign export ccall hs_parse :: CString -> CString -> CLong -> IO CString
hs_parse :: CString -> CString -> CLong -> IO CString
hs_parse text lang time = do
   hs_text <- peekCString text
   hs_lang <- peekCString lang
   utcNow <- getCurrentTime
   case hs_text of 
       [] -> do
         newCString "need some text"
       _ -> do
         refTime <- return $ _makeReftime (TimeZoneSeries utc []) (millisToUTC $ fromIntegral time)
         let
           context = Context
                     { referenceTime = refTime
                     , lang = parseLang hs_lang
                     }
           parsedResult = parse (Text.pack hs_text) context [This Time]
         newCString $ Text.unpack $ toJText parsedResult
       where
         utcNow = getCurrentTime
         defaultLang = EN

         parseLang :: String -> Lang
         parseLang l = fromMaybe defaultLang $ readMaybe (Text.unpack $ Text.toUpper $ Text.pack l)

         
hs_parse_old :: CString -> CString -> IO CString
hs_parse_old text lang = do
     hs_parse text lang 0
