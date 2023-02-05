import React, { useState, useEffect } from 'react'

export const useFetch = (url: string, options?: object) => {
    const [response, setResponse] = useState<any>({});
    const [error, setError] = useState<any>({});

    useEffect(() => {
      const fetchData = async () => {
        try {
          const res = await fetch(url, options);
          const json = await res.json();
          setResponse(json);
        } catch (error) {
          setError(error);
        }
      };
      fetchData();
    }, );

    return { response, error };
  };